%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	SKey
Summary:	Crypt::SKey - Perl S/Key calculator
Summary(pl):	Crypt::SKey - perlowy kalkulator kluczy S/Key
Name:		perl-Crypt-SKey
Version:	0.06
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
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
%{__perl} -MExtUtils::MakeMaker -we 'WriteMakefile(NAME=>"Crypt::SKey",PL_FILES=>{})'
%{__make}
# disabled - one test is interactive
#%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_sitelib}/Crypt/SKey.pm
%{_mandir}/man3/*
