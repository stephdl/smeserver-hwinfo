# $Id: smeserver-hwinfo.spec,v 1.2 2013/07/14 22:38:09 unnilennium Exp $
# Authority: gnujpl
# Name: Jean-Paul Leclère

%define name smeserver-hwinfo
%define version 1.0
%define release 21

Summary: Harware info panel for SME Server.
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: System Environment/Daemons
Source: %{name}-%{version}.tar.gz
BuildRequires: e-smith-devtools
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires: e-smith-base lshw
Requires: e-smith-formmagick >= 1.4.0-12
Obsoletes: eos-hwinfo
AutoReqProv: no

%description
smeserver-hwinfo adds panel providing informations about server harware configuration
 
%changelog
* Sun Jul 14 2013 JP Pialasse <tests@pialasse.com> 1.0-21.sme
- apply locale 2013-07-14 patch

* Sun Mar 06 2011 SME Translation Server <translations@contribs.org> 1.0-20.sme
- apply locale 2011-03-06 patch

* Tue Oct 27 2009 SME Translation Server <translations@contribs.org> 1.0-19.sme
- apply locale 2009-10-27 patch

* Mon Aug 24 2009 SME Translation Server <translations@contribs.org> 1.0-18.sme
- apply locale 2009-08-24 patch

* Wed May 20 2009 SME Translation Server <translations@contribs.org> 1.0-17.sme
- apply locale 2009-05-20 patch

* Mon Apr 27 2009 SME Translation Server <translations@contribs.org> 1.0-16.sme
- apply locale 2009-04-27 patch

* Tue Mar 03 2009 SME Translation Server
- apply locale 2009-03-03 patch

* Sun Mar  1 2009 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0-14
- Apply  1 Mar 2009 locale patch [SME: 5018]

* Tue Oct 14 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0-13
- Apply 14 Oct 2008 locale patch

* Sun Sep 28 2008 Stephen Noble <support@dungog.net> - 1.0-12
- Apply locale patch

* Tue Jul 1 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0-11
- Apply 1 July 2008 locale patch

* Thu May 21 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0-10
- Apply 21 May 2008 locale patch

* Mon May 5 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0-9
- Apply 5 May 2008 locale patch

* Sat Apr 26 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0-8
- Add common <base> tags to e-smith-formmagick's general

* Thu Apr 24 2008 Jean-Paul Leclere <jean-paul@leclere.org> 1.0-7
- remove obsolete httpd templates fragments

* Tue Apr 22 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0-6
- Added e-smith-devtools as build requirement for the createlinks script

* Tue Apr 22 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0-5
- Trying to fix creatlinks build error

* Tue Apr 22 2008 Jonathan Martens <smeserver-contribs@snetram.nl> 1.0-4
- Added 22 April 2008 locale patch

* Fri Apr 4 2008 Jean-Paul Leclere <jean-paul@leclere.org>
- [1.0-3]
- removing duplicate template fragment

* Sun Jan 20 2008 Jean-Paul Leclere <jean-paul@leclere.org>
- [1.0-2]
- templates-custom replacement by templates fragment
- change Copyright to License in spec

* Fri Aug 24 2007 Jean-Paul Leclere <jean-paul@leclere.org>
- [1.0-1]
- port from Free-EOS eos-hwinfo, as a new panel in server-manager

%prep
%setup

%pre

%post

%build
perl createlinks 

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f e-smith-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-filelist

%preun

%postun

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-filelist
%defattr(0644,root,root)


