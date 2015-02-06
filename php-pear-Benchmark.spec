%define		_class		Benchmark
%define		upstream_name	%{_class}

Name:		php-pear-%{upstream_name}
Version:	1.2.9
Release:	3
Summary:	Benchmark PHP scripts or function calls
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Benchmark/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
Framework to benchmark PHP scripts or function calls.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests
rm -rf %{buildroot}%{_datadir}/pear/data

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/doc/*.php
%doc %{upstream_name}-%{version}/LICENSE
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Sun Dec 18 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.9-1mdv2012.0
+ Revision: 743483
- 1.2.9

* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.8-3
+ Revision: 741826
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.8-2
+ Revision: 679265
- mass rebuild

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.8-1mdv2011.0
+ Revision: 602116
- new version

* Wed Dec 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.7-6mdv2010.1
+ Revision: 479362
- use package2.xml, fix installation path

* Sun Dec 13 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.7-5mdv2010.1
+ Revision: 478305
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.2.7-4mdv2010.0
+ Revision: 440944
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.2.7-3mdv2009.1
+ Revision: 321901
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2.7-2mdv2009.0
+ Revision: 236805
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jul 23 2007 Oden Eriksson <oeriksson@mandriva.com> 1.2.7-1mdv2008.0
+ Revision: 54602
- fix build
- 1.2.7


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.6-1mdv2007.0
+ Revision: 81394
- Import php-pear-Benchmark

* Sat May 20 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.6-1mdk
- 1.2.6

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.4-1mdk
- 1.2.4
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.3-4mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.3-3mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.3-2mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.3-1mdk
- 1.2.3

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.2-1mdk
- initial Mandriva package (PLD import)

