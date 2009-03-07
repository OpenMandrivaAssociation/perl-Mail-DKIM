%define module Mail-DKIM

Name:		perl-%{module}
Version:	0.32
Release:	%mkrel 3
Summary:	Implements DomainKeys Identified Mail (DKIM)
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Mail/%{module}-%{version}.tar.gz
BuildRequires:	perl-Module-Build
BuildRequires:	perl-Test-Pod
BuildRequires:	perl(Crypt::OpenSSL::RSA)
BuildRequires:	perl(Digest::SHA)
BuildRequires:	perl(Digest::SHA1)
BuildRequires:	perl(Mail::Address)
BuildRequires:	perl(MIME::Base64)
BuildRequires:	perl(Net::DNS)
BuildRequires:	perl(Test::Simple)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module implements the various components of the DKIM and DomainKeys
message-signing and verifying standards for Internet mail. It currently
tries to implement these specifications:
 * RFC4871, for DKIM
 * RFC4870, for DomainKeys

%prep

%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}

%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc scripts Changes README TODO
%dir %{perl_vendorlib}/Mail/DKIM
%dir %{perl_vendorlib}/Mail/DKIM/Algorithm
%dir %{perl_vendorlib}/Mail/DKIM/Canonicalization
%{perl_vendorlib}/Mail/DKIM/*.pm
%{perl_vendorlib}/Mail/DKIM/Algorithm/*.pm
%{perl_vendorlib}/Mail/DKIM/Canonicalization/*.pm
%{perl_vendorlib}/Mail/DKIM.pm
%{_mandir}/man3/*

