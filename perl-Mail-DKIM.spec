%define upstream_name    Mail-DKIM
%define upstream_version 0.39

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4
Summary:	Implements DomainKeys Identified Mail (DKIM)
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Mail/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-Module-Build
BuildRequires:	perl-Test-Pod
BuildRequires:	perl(Crypt::OpenSSL::RSA)
BuildRequires:	perl(Digest::SHA)
BuildRequires:	perl(Digest::SHA1)
BuildRequires:	perl(Mail::Address)
BuildRequires:	perl(MIME::Base64)
BuildRequires:	perl(Net::DNS)
BuildRequires:	perl(Test::Simple)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This module implements the various components of the DKIM and DomainKeys
message-signing and verifying standards for Internet mail. It currently
tries to implement these specifications:
 * RFC4871, for DKIM
 * RFC4870, for DomainKeys

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
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


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.390.0-2mdv2011.0
+ Revision: 667248
- mass rebuild

* Tue Nov 16 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.390.0-1mdv2011.0
+ Revision: 598084
- update to new version 0.39

* Fri Apr 30 2010 Giuseppe Ghibò <ghibo@mandriva.com> 0.380.0-3mdv2011.0
+ Revision: 541311
- Fix condition as 2010.0 has %%perl_convert_version macro.
- Fix Release number to be backportable (es. for MES5).

* Tue Apr 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.380.0-1mdv2010.1
+ Revision: 536964
- update to 0.38

* Wed Sep 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.370.0-1mdv2010.0
+ Revision: 434689
- update to new version 0.37

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.360.0-1mdv2010.0
+ Revision: 402574
- rebuild using %%perl_convert_version

* Sun Jun 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.36-1mdv2010.0
+ Revision: 383528
- update to new version 0.36

* Sun May 24 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.35-1mdv2010.0
+ Revision: 379183
- update to new version 0.35

* Thu May 21 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.34-1mdv2010.0
+ Revision: 378232
- update to new version 0.34

* Wed Mar 11 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.33-1mdv2009.1
+ Revision: 353615
- update to new version 0.33

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.32-3mdv2009.1
+ Revision: 351900
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild early 2009.0 package (before pixel changes)

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - new version

* Thu Apr 24 2008 Oden Eriksson <oeriksson@mandriva.com> 0.31-0mdv2009.0
+ Revision: 197172
- import perl-Mail-DKIM


* Thu Apr 24 2008 Oden Eriksson <oeriksson@mandriva.com> 0.31-1mdv2009.0
- initial Mandriva package 
