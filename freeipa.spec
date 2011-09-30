# TODO
# - build deps:
#        /usr/share/selinux/devel/Makefile is needed by freeipa-2.1.0-0.1.src
#        389-ds-base-devel >= 1.2.9 is needed by freeipa-2.1.0-0.1.src
#        authconfig is needed by freeipa-2.1.0-0.1.src
#        krb5-devel is needed by freeipa-2.1.0-0.1.src
#        krb5-workstation is needed by freeipa-2.1.0-0.1.src
#        libipa_hbac-python is needed by freeipa-2.1.0-0.1.src
#        policycoreutils >= %{POLICYCOREUTILSVER} is needed by freeipa-2.1.0-0.1.src
#        pylint is needed by freeipa-2.1.0-0.1.src
#        python-kerberos is needed by freeipa-2.1.0-0.1.src
#        python-krbV is needed by freeipa-2.1.0-0.1.src
#        python-ldap is needed by freeipa-2.1.0-0.1.src
#        python-netaddr >= 0.7.5-3 is needed by freeipa-2.1.0-0.1.src
#        python-nss is needed by freeipa-2.1.0-0.1.src
#        python-rhsm is needed by freeipa-2.1.0-0.1.src

Summary:	The Identity, Policy and Audit system
Name:		freeipa
Version:	2.1.0
Release:	0.1
License:	GPL v3+
Group:		Base
URL:		http://www.freeipa.org/
Source0:	http://www.freeipa.org/downloads/src/%{name}-%{version}.tar.gz
# Source0-md5:	2272a05e8d09a009a999e4fef25588a6
BuildRequires:	/usr/share/selinux/devel/Makefile
BuildRequires:	389-ds-base-devel >= 1.2.9
BuildRequires:	authconfig
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel >= 7.21.3-9
BuildRequires:	gettext
BuildRequires:	krb5-devel
BuildRequires:	krb5-workstation
BuildRequires:	libipa_hbac-python
BuildRequires:	libtool
BuildRequires:	libuuid-devel
BuildRequires:	m4
BuildRequires:	nspr-devel
BuildRequires:	nss-devel
BuildRequires:	openldap-devel
BuildRequires:	openssl-devel
BuildRequires:	policycoreutils >= %{POLICYCOREUTILSVER}
BuildRequires:	popt-devel
BuildRequires:	pylint
BuildRequires:	python-devel
BuildRequires:	python-kerberos
BuildRequires:	python-krbV
BuildRequires:	python-ldap
BuildRequires:	python-netaddr >= 0.7.5-3
BuildRequires:	python-nss
BuildRequires:	python-pyOpenSSL
BuildRequires:	python-rhsm
BuildRequires:	python-setuptools
BuildRequires:	svrcore-devel
BuildRequires:	xmlrpc-c-devel >= 1.25.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		httpd_conf			/etc/httpd/conf.d
%define		plugin_dir			%{_libdir}/dirsrv/plugins
%define		POLICYCOREUTILSVER	1.33.12-1
%define		gettext_domain		ipa

%description
IPA is an integrated solution to provide centrally managed Identity
(machine, user, virtual machines, groups, authentication credentials),
Policy (configuration settings, access control information) and Audit
(events, logs, analysis thereof).

%package server
Summary:	The IPA authentication server
Group:		Base
Requires:	%{name}-admintools = %{version}-%{release}
Requires:	%{name}-client = %{version}-%{release}
Requires:	%{name}-python = %{version}-%{release}
Requires(post):	%{name}-server-selinux = %{version}-%{release}
Requires(pre):	389-ds-base >= 1.2.9.6-1
Requires:	acl
Requires:	apache-mod_wsgi
Requires:	cyrus-sasl-gssapi%{?_isa}
Requires:	httpd
Requires:	krb5-pkinit-openssl
Requires:	krb5-server
Requires:	krb5-server-ldap
Requires:	mod_auth_kerb
Requires:	mod_nss >= 1.0.8-10
Requires:	nss
Requires:	nss-tools
Requires:	ntp
Requires:	openldap-clients
Requires:	python-krbV
Requires:	python-ldap
Requires:	python-pyasn1 >= 0.0.9a
Requires:	selinux-policy >= 3.9.16-18
Requires(post):	selinux-policy-base
Requires:	dogtag-pki-ca-theme
Requires:	dogtag-pki-common-theme
Requires:	pki-ca >= 9.0.11
Requires:	pki-silent >= 9.0.11
Requires:	slapi-nis >= 0.21
Requires(preun):	python initscripts chkconfig
Requires(postun):	python initscripts chkconfig
Obsoletes:	ipa-server >= 1.0

%description server
IPA is an integrated solution to provide centrally managed Identity
(machine, user, virtual machines, groups, authentication credentials),
Policy (configuration settings, access control information) and Audit
(events, logs, analysis thereof). If you are installing an IPA server
you need to install this package (in other words, most people should
NOT install this package).


%package server-selinux
Summary:	SELinux rules for freeipa-server daemons
Group:		Base
Requires:	%{name}-server = %{version}-%{release}
Requires(pre):	policycoreutils >= %{POLICYCOREUTILSVER}
Obsoletes:	ipa-server-selinux >= 1.0

%description server-selinux
IPA is an integrated solution to provide centrally managed Identity
(machine, user, virtual machines, groups, authentication credentials),
Policy (configuration settings, access control information) and Audit
(events, logs, analysis thereof). This package provides SELinux rules
for the daemons included in freeipa-server

%package client
Summary:	IPA authentication for use on clients
Group:		Base
Requires:	%{name}-python = %{version}-%{release}
Requires:	authconfig
Requires:	bind-utils
Requires:	certmonger >= 0.26
Requires:	cyrus-sasl-gssapi%{?_isa}
Requires:	krb5-workstation
Requires:	libcurl >= 7.21.3-9
Requires:	nss-tools
Requires:	ntp
Requires:	pam_krb5
Requires:	python-ldap
Requires:	sssd >= 1.5.1
Requires:	wget
Requires:	xmlrpc-c >= 1.25.4
Obsoletes:	ipa-client >= 1.0

%description client
IPA is an integrated solution to provide centrally managed Identity
(machine, user, virtual machines, groups, authentication credentials),
Policy (configuration settings, access control information) and Audit
(events, logs, analysis thereof). If your network uses IPA for
authentication, this package should be installed on every client
machine.

%package admintools
Summary:	IPA administrative tools
Group:		Base
Requires:	%{name}-client = %{version}-%{release}
Requires:	%{name}-python = %{version}-%{release}
Requires:	python-krbV
Requires:	python-ldap
Obsoletes:	ipa-admintools >= 1.0

%description admintools
IPA is an integrated solution to provide centrally managed Identity
(machine, user, virtual machines, groups, authentication credentials),
Policy (configuration settings, access control information) and Audit
(events, logs, analysis thereof). This package provides command-line
tools for IPA administrators.

%package python
Summary:	Python libraries used by IPA
Group:		Libraries
Requires:	python-kerberos >= 1.1-3
Requires:	authconfig
Requires:	gnupg
Requires:	iproute2
Requires:	libipa_hbac-python
Requires:	python-lxml
Requires:	python-netaddr >= 0.7.5-3
Requires:	python-nss >= 0.11
Requires:	python-pyOpenSSL
Obsoletes:	ipa-python >= 1.0

%description python
IPA is an integrated solution to provide centrally managed Identity
(machine, user, virtual machines, groups, authentication credentials),
Policy (configuration settings, access control information) and Audit
(events, logs, analysis thereof). If you are using IPA you need to
install this package.

%prep
%setup -q

%build
export CFLAGS="$CFLAGS %{optflags}"
export CPPFLAGS="$CPPFLAGS %{optflags}"
%{__make} version-update

cd ipa-client
../autogen.sh \
	--prefix=%{_usr} \
	--sysconfdir=%{_sysconfdir} \
	--localstatedir=%{_localstatedir} \
	--libdir=%{_libdir} \
	--mandir=%{_mandir}

cd ../daemons
../autogen.sh \
	--prefix=%{_usr} \
	--sysconfdir=%{_sysconfdir} \
	--localstatedir=%{_localstatedir} \
	--libdir=%{_libdir} \
	--mandir=%{_mandir} \
	--with-openldap

cd ../install
../autogen.sh \
	--prefix=%{_usr} \
	--sysconfdir=%{_sysconfdir} \
	--localstatedir=%{_localstatedir} \
	--libdir=%{_libdir} \
	--mandir=%{_mandir}

cd ..

%{__make} all IPA_VERSION_IS_GIT_SNAPSHOT=no

cd selinux
# This isn't multi-process make capable yet
%{__make} all -j1

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C selinux install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{gettext_domain}

# Remove .la files from libtool - we don't want to package
# these files
rm $RPM_BUILD_ROOT/%{plugin_dir}/libipa_pwd_extop.la
rm $RPM_BUILD_ROOT/%{plugin_dir}/libipa_enrollment_extop.la
rm $RPM_BUILD_ROOT/%{plugin_dir}/libipa_winsync.la
rm $RPM_BUILD_ROOT/%{plugin_dir}/libipa_repl_version.la
rm $RPM_BUILD_ROOT/%{plugin_dir}/libipa_uuid.la
rm $RPM_BUILD_ROOT/%{plugin_dir}/libipa_modrdn.la
rm $RPM_BUILD_ROOT/%{plugin_dir}/libipa_lockout.la

# Some user-modifiable HTML files are provided. Move these to %{_sysconfdir}
# and link back.
install -d $RPM_BUILD_ROOT/%{_sysconfdir}/ipa/html
install -d $RPM_BUILD_ROOT/%{_localstatedir}/cache/ipa/sysrestore
mkdir $RPM_BUILD_ROOT%{_usr}/share/ipa/html/
ln -s ../../../..%{_sysconfdir}/ipa/html/ssbrowser.html \
    $RPM_BUILD_ROOT%{_usr}/share/ipa/html/ssbrowser.html
ln -s ../../../..%{_sysconfdir}/ipa/html/unauthorized.html \
    $RPM_BUILD_ROOT%{_usr}/share/ipa/html/unauthorized.html
ln -s ../../../..%{_sysconfdir}/ipa/html/browserconfig.html \
    $RPM_BUILD_ROOT%{_usr}/share/ipa/html/browserconfig.html
ln -s ../../../..%{_sysconfdir}/ipa/html/hbac-deny-remove.html \
    $RPM_BUILD_ROOT%{_usr}/share/ipa/html/hbac-deny-remove.html
ln -s ../../../..%{_sysconfdir}/ipa/html/ipa_error.css \
    $RPM_BUILD_ROOT%{_usr}/share/ipa/html/ipa_error.css

# So we can own our Apache configuration
install -d $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d
touch $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/ipa.conf
touch $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d/ipa-rewrite.conf
install ipa.init $RPM_BUILD_ROOT%{_initrddir}/ipa

install -d $RPM_BUILD_ROOT%{_sysconfdir}/ipa
touch $RPM_BUILD_ROOT%{_sysconfdir}/ipa/default.conf
install -p -d $RPM_BUILD_ROOT/%{_localstatedir}/lib/ipa-client/sysrestore

install -d $RPM_BUILD_ROOT/etc/bash_completion.d
install -pm 644 contrib/completion/ipa.bash_completion $RPM_BUILD_ROOT/etc/bash_completion.d/ipa
install -d $RPM_BUILD_ROOT/etc/cron.d
install -pm 644 ipa-compliance.cron $RPM_BUILD_ROOT/etc/cron.d/ipa-compliance

%clean
rm -rf $RPM_BUILD_ROOT

%post server
if [ $1 = 1 ]; then
	/sbin/chkconfig --add ipa
	/sbin/chkconfig --add ipa_kpasswd
fi
if [ $1 -gt 1 ]; then
	%{_sbindir}/ipa-upgradeconfig || :
	%{_sbindir}/ipa-ldap-updater --upgrade >/dev/null 2>&1 || :
fi

%preun server
if [ $1 = 0 ]; then
	/sbin/chkconfig --del ipa
	/sbin/chkconfig --del ipa_kpasswd
	%service ipa stop
fi

%postun server
if [ "$1" -ge "1" ]; then
	%service ipa restart
fi

%pre server-selinux
# Save the content state so we can restore it when/if this package is removed
if [ -s /etc/selinux/config ]; then
	. %{_sysconfdir}/selinux/config
	FILE_CONTEXT=%{_sysconfdir}/selinux/targeted/contexts/files/file_contexts
	if [ "${SELINUXTYPE}" == targeted -a -f ${FILE_CONTEXT} ]; then \
		cp -f ${FILE_CONTEXT} ${FILE_CONTEXT}.%{name}
	fi
fi

%post server-selinux
# Insert our provide SELinux policy
semodule -s targeted -i %{_datadir}/selinux/targeted/ipa_kpasswd.pp %{_datadir}/selinux/targeted/ipa_httpd.pp %{_datadir}/selinux/targeted/ipa_dogtag.pp
. %{_sysconfdir}/selinux/config
FILE_CONTEXT=%{_sysconfdir}/selinux/targeted/contexts/files/file_contexts
selinuxenabled
if [ $? == 0  -a "${SELINUXTYPE}" == targeted -a -f ${FILE_CONTEXT}.%{name} ]; then
   fixfiles -C ${FILE_CONTEXT}.%{name} restore
   rm -f ${FILE_CONTEXT}.%{name}
fi

%preun server-selinux
# On the last uninstallation prepare to restore state
if [ $1 = 0 ]; then
	if [ -s %{_sysconfdir}/selinux/config ]; then
	   . %{_sysconfdir}/selinux/config
	   FILE_CONTEXT=%{_sysconfdir}/selinux/targeted/contexts/files/file_contexts
	   if [ "${SELINUXTYPE}" == targeted -a -f ${FILE_CONTEXT} ]; then \
		   cp -f ${FILE_CONTEXT} ${FILE_CONTEXT}.%{name}
	   fi
	fi
fi

%postun server-selinux
# On the last uninstallation remove our SELinux policy and restore the state
if [ $1 = 0 ]; then
	semodule -s targeted -r ipa_kpasswd ipa_httpd ipa_dogtag
	. %{_sysconfdir}/selinux/config
	FILE_CONTEXT=%{_sysconfdir}/selinux/targeted/contexts/files/file_contexts
	selinuxenabled
	if [ $? == 0  -a "${SELINUXTYPE}" == targeted -a -f ${FILE_CONTEXT}.%{name} ]; then
	   fixfiles -C ${FILE_CONTEXT}.%{name} restore
	   rm -f ${FILE_CONTEXT}.%{name}
	fi
fi

%files server
%defattr(644,root,root,755)
%doc COPYING README Contributors.txt
%attr(755,root,root) %{_sbindir}/ipa-ca-install
%attr(755,root,root) %{_sbindir}/ipa-dns-install
%attr(755,root,root) %{_sbindir}/ipa-server-install
%attr(755,root,root) %{_sbindir}/ipa-replica-conncheck
%attr(755,root,root) %{_sbindir}/ipa-replica-install
%attr(755,root,root) %{_sbindir}/ipa-replica-prepare
%attr(755,root,root) %{_sbindir}/ipa-replica-manage
%attr(755,root,root) %{_sbindir}/ipa-csreplica-manage
%attr(755,root,root) %{_sbindir}/ipa-server-certinstall
%attr(755,root,root) %{_sbindir}/ipa-ldap-updater
%attr(755,root,root) %{_sbindir}/ipa-compat-manage
%attr(755,root,root) %{_sbindir}/ipa-nis-manage
%attr(755,root,root) %{_sbindir}/ipa-host-net-manage
%attr(755,root,root) %{_sbindir}/ipa_kpasswd
%attr(755,root,root) %{_sbindir}/ipactl
%attr(755,root,root) %{_sbindir}/ipa-upgradeconfig
%attr(755,root,root) %{_sbindir}/ipa-compliance
/etc/cron.d/ipa-compliance
%attr(755,root,root) %{_initrddir}/ipa
%attr(755,root,root) %{_initrddir}/ipa_kpasswd
%dir %{py_sitescriptdir}/ipaserver
%{py_sitescriptdir}/ipaserver/*
%dir %{_usr}/share/ipa
%{_usr}/share/ipa/wsgi.py*
%{_usr}/share/ipa/*.ldif
%{_usr}/share/ipa/*.uldif
%{_usr}/share/ipa/*.template
%dir %{_usr}/share/ipa/html
%{_usr}/share/ipa/html/ssbrowser.html
%{_usr}/share/ipa/html/browserconfig.html
%{_usr}/share/ipa/html/unauthorized.html
%{_usr}/share/ipa/html/hbac-deny-remove.html
%{_usr}/share/ipa/html/ipa_error.css
%dir %{_usr}/share/ipa/migration
%{_usr}/share/ipa/migration/error.html
%{_usr}/share/ipa/migration/index.html
%{_usr}/share/ipa/migration/invalid.html
%{_usr}/share/ipa/migration/ipa_migration.css
%{_usr}/share/ipa/migration/migration.py*
%dir %{_usr}/share/ipa/ui
%{_usr}/share/ipa/ui/index.html
%{_usr}/share/ipa/ui/*.png
%{_usr}/share/ipa/ui/*.gif
%{_usr}/share/ipa/ui/*.ico
%{_usr}/share/ipa/ui/*.css
%{_usr}/share/ipa/ui/*.js
%{_usr}/share/ipa/ui/*.eot
%{_usr}/share/ipa/ui/*.svg
%{_usr}/share/ipa/ui/*.ttf
%{_usr}/share/ipa/ui/*.woff
%dir %{_sysconfdir}/ipa
%dir %{_sysconfdir}/ipa/html
%config(noreplace) %{_sysconfdir}/ipa/html/ssbrowser.html
%config(noreplace) %{_sysconfdir}/ipa/html/ipa_error.css
%config(noreplace) %{_sysconfdir}/ipa/html/unauthorized.html
%config(noreplace) %{_sysconfdir}/ipa/html/browserconfig.html
%config(noreplace) %{_sysconfdir}/ipa/html/hbac-deny-remove.html
%ghost %attr(644,root,apache) %config(noreplace) %{_sysconfdir}/httpd/conf.d/ipa-rewrite.conf
%ghost %attr(644,root,apache) %config(noreplace) %{_sysconfdir}/httpd/conf.d/ipa.conf
%{_usr}/share/ipa/ipa.conf
%{_usr}/share/ipa/ipa-rewrite.conf
%dir %{_usr}/share/ipa/updates/
%{_usr}/share/ipa/updates/*
%attr(755,root,root) %{plugin_dir}/libipa_pwd_extop.so
%attr(755,root,root) %{plugin_dir}/libipa_enrollment_extop.so
%attr(755,root,root) %{plugin_dir}/libipa_winsync.so
%attr(755,root,root) %{plugin_dir}/libipa_repl_version.so
%attr(755,root,root) %{plugin_dir}/libipa_uuid.so
%attr(755,root,root) %{plugin_dir}/libipa_modrdn.so
%attr(755,root,root) %{plugin_dir}/libipa_lockout.so
%dir %{_localstatedir}/lib/ipa
%attr(700,root,root) %dir %{_localstatedir}/lib/ipa/sysrestore
%dir %{_localstatedir}/cache/ipa
%attr(700,apache,apache) %dir %{_localstatedir}/cache/ipa/sessions
%attr(700,root,root) %dir %{_localstatedir}/cache/ipa/kpasswd
%{_mandir}/man1/ipa-replica-conncheck.1*
%{_mandir}/man1/ipa-replica-install.1*
%{_mandir}/man1/ipa-replica-manage.1*
%{_mandir}/man1/ipa-csreplica-manage.1*
%{_mandir}/man1/ipa-replica-prepare.1*
%{_mandir}/man1/ipa-server-certinstall.1*
%{_mandir}/man1/ipa-server-install.1*
%{_mandir}/man1/ipa-dns-install.1*
%{_mandir}/man1/ipa-ca-install.1*
%{_mandir}/man1/ipa-compat-manage.1*
%{_mandir}/man1/ipa-nis-manage.1*
%{_mandir}/man1/ipa-host-net-manage.1*
%{_mandir}/man1/ipa-ldap-updater.1*
%{_mandir}/man8/ipa_kpasswd.8*
%{_mandir}/man8/ipactl.8*
%{_mandir}/man1/ipa-compliance.1*

%files server-selinux
%defattr(644,root,root,755)
%doc COPYING README Contributors.txt
%{_usr}/share/selinux/targeted/ipa_kpasswd.pp
%{_usr}/share/selinux/targeted/ipa_httpd.pp
%{_usr}/share/selinux/targeted/ipa_dogtag.pp

%files client
%defattr(644,root,root,755)
%doc COPYING README Contributors.txt
%attr(755,root,root) %{_sbindir}/ipa-client-install
%attr(755,root,root) %{_sbindir}/ipa-getkeytab
%attr(755,root,root) %{_sbindir}/ipa-rmkeytab
%attr(755,root,root) %{_sbindir}/ipa-join
%dir %{_usr}/share/ipa
%dir %{_usr}/share/ipa/ipaclient
%dir %{_localstatedir}/lib/ipa-client
%dir %{_localstatedir}/lib/ipa-client/sysrestore
%{_usr}/share/ipa/ipaclient/ipa.cfg
%{_usr}/share/ipa/ipaclient/ipa.js
%dir %{py_sitescriptdir}/ipaclient
%{py_sitescriptdir}/ipaclient/*.py*
%{_mandir}/man1/ipa-getkeytab.1*
%{_mandir}/man1/ipa-rmkeytab.1*
%{_mandir}/man1/ipa-client-install.1*
%{_mandir}/man1/ipa-join.1*
%{_mandir}/man5/default.conf.5*

%files admintools
%defattr(644,root,root,755)
%doc COPYING README Contributors.txt
%config %{_sysconfdir}/bash_completion.d
%attr(755,root,root) %{_bindir}/ipa
%{_mandir}/man1/ipa.1*

%files python -f %{gettext_domain}.lang
%defattr(644,root,root,755)
%doc COPYING README Contributors.txt
%ghost %attr(644,root,apache) %config(noreplace) %{_sysconfdir}/ipa/default.conf
%dir %{py_sitescriptdir}/ipapython
%{py_sitescriptdir}/ipapython/*.py*
%dir %{py_sitescriptdir}/ipalib
%{py_sitescriptdir}/ipalib/*
%{py_sitedir}/default_encoding_utf8.so
%{py_sitescriptdir}/ipapython-*.egg-info
%{py_sitescriptdir}/freeipa-*.egg-info
%{py_sitedir}/python_default_encoding-*.egg-info
