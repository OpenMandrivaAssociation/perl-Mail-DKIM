%define modname	Mail-DKIM

Summary:	Implements DomainKeys Identified Mail (DKIM)
Name:		perl-%{modname}
Version:	1.20261105
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{modname}
Source0:	https://cpan.metacpan.org/authors/id/M/MB/MBRADSHAW/Mail-DKIM-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl-Module-Build
BuildRequires:	perl-Test-Pod
BuildRequires:	perl(Crypt::OpenSSL::RSA)
BuildRequires:	perl(Crypt::PK::Ed25519)
BuildRequires:	perl(Digest::SHA)
BuildRequires:	perl(Digest::SHA1)
BuildRequires:	perl(Mail::Address)
BuildRequires:	perl(MIME::Base64)
BuildRequires:	perl(Net::DNS)
BuildRequires:	perl(Test::Simple)
BuildRequires:	perl(Mail::AuthenticationResults)
BuildRequires:	perl(Mail::AuthenticationResults::Header::AuthServID)
BuildRequires:	perl(Mail::AuthenticationResults::Parser)
BuildRequires:	perl-devel

Requires:	perl(Crypt::PK::Ed25519)
Requires:	perl(Mail::AuthenticationResults)
Requires:	perl(Mail::AuthenticationResults::Header::AuthServID)
Requires:	perl(Mail::AuthenticationResults::Parser)

%description
This module implements the various components of the DKIM and DomainKeys
message-signing and verifying standards for Internet mail. It currently
tries to implement these specifications:
 * RFC4871, for DKIM
 * RFC4870, for DomainKeys

%prep
%autosetup -p1 -n %{modname}-%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%install
%make_install

%files
%doc scripts Changes README.md TODO
%dir %{perl_vendorlib}/Mail/DKIM
%dir %{perl_vendorlib}/Mail/DKIM/Algorithm
%dir %{perl_vendorlib}/Mail/DKIM/Canonicalization
%{perl_vendorlib}/Mail/DKIM/*.pm
%{perl_vendorlib}/Mail/DKIM/ARC
%{perl_vendorlib}/Mail/DKIM/Algorithm/*.pm
%{perl_vendorlib}/Mail/DKIM/Canonicalization/*.pm
%{perl_vendorlib}/Mail/DKIM.pm
#{perl_vendorlib}/Mail/sample_mime_lite.pl
%{_mandir}/man3/*


