#
# Conditional build:
%bcond_with	tests	# perform "make test"
			# disabled by default - one test is interactive
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Crypt
%define	pnam	SKey
Summary:	Crypt::SKey - Perl S/Key calculator
Summary(pl):	Crypt::SKey - perlowy kalkulator kluczy S/Key
Name:		perl-Crypt-SKey
Version:	0.06
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2036f6f218941da859036d70cb53b169
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Digest-MD4
BuildRequires:	perl-Term-ReadKey
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module contains a simple S/Key calculator (as described in RFC
1760) implemented in Perl.

%description -l pl
Ten modu³ zawiera prosty kalkulator do kluczy S/Key (zgodny z opisem
z RFC 1760), zaimplementowany w Perlu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} -MExtUtils::MakeMaker -we 'WriteMakefile(NAME=>"Crypt::SKey",PL_FILES=>{})' \
	INSTALLDIRS=vendor
%{__make}

# disabled by default - one test is interactive
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Crypt/SKey.pm
%{_mandir}/man3/*
