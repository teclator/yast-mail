#
# spec file for package yast2-mail
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           yast2-mail
Version:        3.1.6
Release:        0

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.bz2


Group:	        System/YaST
License:        GPL-2.0+
BuildRequires:	perl-XML-Writer update-desktop-files yast2-testsuite
BuildRequires:  yast2-devtools >= 3.1.10
BuildRequires:	yast2-auth-server yast2-network yast2-perl-bindings yast2-users
BuildRequires:  perl-NetxAP

PreReq:         %fillup_prereq

# new firewall interface
# Wizard::SetDesktopTitleAndIcon
Requires:	yast2 >= 2.21.22
Requires:	yast2-users
Requires:	yast2-ldap
Provides:	yast2-config-network:/usr/lib/YaST2/clients/lan_sendmail.ycp
Provides:	yast2-config-sendmail yast2-config-sendmail-devel
Obsoletes:	yast2-config-sendmail yast2-config-sendmail-devel
Provides:       yast2-trans-sendmail = %{version}
Obsoletes:      yast2-trans-sendmail <= %{version}
Provides:       yast2-config-mail = %{version}
Obsoletes:      yast2-config-mail <= %{version}
Provides:       yast2-trans-mail = %{version}
Obsoletes:      yast2-trans-mail <= %{version}
Provides:       yast2-mail-server = %{version}
Obsoletes:      yast2-mail-server <= %{version}
Provides:       yast2-mail-plugins = %{version}
Obsoletes:      yast2-mail-plugins <= %{version}
Conflicts:	aaa_base < 10.3
BuildArch:	noarch
Requires:       yast2-ruby-bindings >= 1.0.0

Summary:	YaST2 - Mail Configuration

%description
The YaST2 component for mail configuration. It handles Postfix, Cyrus,
Amavis and Fetchmail.

%prep
%setup -n %{name}-%{version}

%build
%yast_build

%install
%yast_install


%post
%{fillup_only -n mail}

%files
%defattr(-,root,root)
%dir %{yast_yncludedir}/mail
%{yast_yncludedir}/mail/*
%dir %{yast_clientdir}
%{yast_clientdir}/mail*
%dir %{yast_moduledir}
%{yast_moduledir}/Mail.rb
%dir %{yast_desktopdir}
%{yast_desktopdir}/mail.desktop
%dir %{yast_schemadir}/autoyast/rnc
%{yast_schemadir}/autoyast/rnc/mail.rnc
%{yast_scrconfdir}/*
%dir %{yast_agentdir}
%{yast_agentdir}/ag_fetchmailrc
%{yast_agentdir}/ag_mailconfig
%{yast_agentdir}/ag_mail_ldaptable
%{yast_agentdir}/ag_mailtable
%{yast_agentdir}/ag_smtp_auth
%{yast_agentdir}/MasterCFParser.pm
%{yast_agentdir}/ag_fetchmailrc
%{yast_agentdir}/ag_mailtable
%attr(0755,root,root) %{yast_agentdir}/setup_dkim_verifying.pl

%dir /etc/openldap/
%dir /etc/openldap/schema/
/etc/openldap/schema/suse-mailserver.schema
%doc %{yast_docdir}


/var/adm/fillup-templates/sysconfig.mail

