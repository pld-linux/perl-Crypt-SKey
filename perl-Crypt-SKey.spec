%include	/usr/lib/rpm/macros.perl
%define		pdir	Crypt
%define		pnam	SKey
Summary:	Crypt::SKey Perl module - Perl S/Key calculator
Summary(pl):	Modu� Perla Crypt::SKey - perlowy kalkulator kluczy S/Key
Name:		perl-Crypt-SKey
Version:	0.03
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
Requires:	perl-Term-ReadKey
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module contains a simple S/Key calculator (as described in RFC
1760) implemented in Perl.

%description -l pl
Ten modu� zawiera prosty kalkulator do kluczy S/Key (zgodny z opisem
z RFC 1760), zaimplementowany w Perlu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
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
%doc Changes README
%{perl_sitelib}/Crypt/SKey.pm
%{_mandir}/man3/*
