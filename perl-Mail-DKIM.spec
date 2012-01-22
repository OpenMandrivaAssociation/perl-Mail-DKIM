%define upstream_name    Mail-DKIM
%define upstream_version 0.39

Name:		perl-%{upstream_name}
%if %{mdkversion} < 201000
Version:	%{upstream_version}
%else
Version:	%perl_convert_version %{upstream_version}
%endif
Release:	%mkrel 4
Summary:	Implements DomainKeys Identified Mail (DKIM)
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Mail/%{upstream_name}-%{upstream_version}.tar.gz

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
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module implements the various components of the DKIM and DomainKeys
message-signing and verifying standards for Internet mail. It currently
tries to implement these specifications:
 * RFC4871, for DKIM
 * RFC4870, for DomainKeys

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

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
%{perl_vendorlib}/Mail/sample_mime_lite.pl
%{_mandir}/man3/*
