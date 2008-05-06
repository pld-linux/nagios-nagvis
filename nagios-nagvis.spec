Summary:	Nagios Visualisation Addon
Name:		nagios-nagvis
Version:	1.2.2
Release:	0.1
License:	GPL
Group:		Applications/WWW
URL:		http://www.nagvis.org/
Source0:	http://dl.sourceforge.net/nagvis/nagvis-%{version}.tar.gz
# Source0-md5:	ffe2764e5f76f8a68bbb1737ea8fd432
Source1:	http://dl.sourceforge.net/nagvis/NagVis-Iconset-Standard-Mini-0.1.tar.gz
# Source1-md5:	6678111581f3bb5400ab77d1f9eab8d0
Source2:	http://dl.sourceforge.net/nagvis/NagVis-Shapes-Server-Nuvola.tar.gz
# Source2-md5:	a88970bd07d665e86ed6237f8830896b
Source3:	%{name}-config.ini.php
Source4:	%{name}-map.cfg
Requires:	webserver(php)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_datadir}/nagvis
%define		_sysconfdir	/etc/nagvis

%description
NagVis is a visualization addon for Nagios. NagVis can be used to
visualize Nagios data, e.g. to display IT processes like a mail system
or a network infrastructure.

%prep
%setup -q -n nagvis-%{version}

rm -f etc/.htaccess
mv etc sample

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_appdir}}
cp -a *.php nagvis wui $RPM_BUILD_ROOT%{_appdir}
install %{SOURCE3} -D $RPM_BUILD_ROOT%{_sysconfdir}/config.ini.php
install %{SOURCE4} -D $RPM_BUILD_ROOT%{_sysconfdir}/maps/localhost.cfg
tar xzf %{SOURCE1} -C $RPM_BUILD_ROOT%{_appdir}/nagvis/images/iconsets
tar xzf %{SOURCE2} -C $RPM_BUILD_ROOT%{_appdir}/nagvis/images/shapes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc INSTALL LICENCE README
%doc sample
%dir %attr(750,root,http) %{_sysconfdir}
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*.php
%dir %attr(750,root,http) %{_sysconfdir}/maps
%attr(640,root,http) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/maps/*.cfg
%{_appdir}
