#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Log-Dispatch
Version  : 2.70
Release  : 22
URL      : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Log-Dispatch-2.70.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Log-Dispatch-2.70.tar.gz
Summary  : 'Dispatches messages to one or more outputs'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Log-Dispatch-license = %{version}-%{release}
Requires: perl-Log-Dispatch-perl = %{version}-%{release}
Requires: perl(MIME::Lite)
Requires: perl(Mail::Sender)
Requires: perl(Mail::Sendmail)
BuildRequires : buildreq-cpan
BuildRequires : perl(Devel::GlobalDestruction)
BuildRequires : perl(Dist::CheckConflicts)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Params::ValidationCompiler)
BuildRequires : perl(Specio)
BuildRequires : perl(Specio::Declare)
BuildRequires : perl(Specio::Exporter)
BuildRequires : perl(Specio::Library::Builtins)
BuildRequires : perl(Specio::Library::Numeric)
BuildRequires : perl(Specio::Library::String)
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Test::Needs)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(namespace::autoclean)

%description
# NAME
Log::Dispatch - Dispatches messages to one or more outputs
# VERSION
version 2.70

%package dev
Summary: dev components for the perl-Log-Dispatch package.
Group: Development
Provides: perl-Log-Dispatch-devel = %{version}-%{release}
Requires: perl-Log-Dispatch = %{version}-%{release}

%description dev
dev components for the perl-Log-Dispatch package.


%package license
Summary: license components for the perl-Log-Dispatch package.
Group: Default

%description license
license components for the perl-Log-Dispatch package.


%package perl
Summary: perl components for the perl-Log-Dispatch package.
Group: Default
Requires: perl-Log-Dispatch = %{version}-%{release}

%description perl
perl components for the perl-Log-Dispatch package.


%prep
%setup -q -n Log-Dispatch-2.70
cd %{_builddir}/Log-Dispatch-2.70

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Log-Dispatch
cp %{_builddir}/Log-Dispatch-2.70/LICENSE %{buildroot}/usr/share/package-licenses/perl-Log-Dispatch/5586816d65cedc4c52fb3e6704d529fb9535d8fe
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Log::Dispatch.3
/usr/share/man/man3/Log::Dispatch::ApacheLog.3
/usr/share/man/man3/Log::Dispatch::Base.3
/usr/share/man/man3/Log::Dispatch::Code.3
/usr/share/man/man3/Log::Dispatch::Email.3
/usr/share/man/man3/Log::Dispatch::Email::MIMELite.3
/usr/share/man/man3/Log::Dispatch::Email::MailSend.3
/usr/share/man/man3/Log::Dispatch::Email::MailSender.3
/usr/share/man/man3/Log::Dispatch::Email::MailSendmail.3
/usr/share/man/man3/Log::Dispatch::File.3
/usr/share/man/man3/Log::Dispatch::File::Locked.3
/usr/share/man/man3/Log::Dispatch::Handle.3
/usr/share/man/man3/Log::Dispatch::Null.3
/usr/share/man/man3/Log::Dispatch::Output.3
/usr/share/man/man3/Log::Dispatch::Screen.3
/usr/share/man/man3/Log::Dispatch::Syslog.3
/usr/share/man/man3/Log::Dispatch::Types.3
/usr/share/man/man3/Log::Dispatch::Vars.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Log-Dispatch/5586816d65cedc4c52fb3e6704d529fb9535d8fe

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Log/Dispatch.pm
/usr/lib/perl5/vendor_perl/5.34.0/Log/Dispatch/ApacheLog.pm
/usr/lib/perl5/vendor_perl/5.34.0/Log/Dispatch/Base.pm
/usr/lib/perl5/vendor_perl/5.34.0/Log/Dispatch/Code.pm
/usr/lib/perl5/vendor_perl/5.34.0/Log/Dispatch/Conflicts.pm
/usr/lib/perl5/vendor_perl/5.34.0/Log/Dispatch/Email.pm
/usr/lib/perl5/vendor_perl/5.34.0/Log/Dispatch/Email/MIMELite.pm
/usr/lib/perl5/vendor_perl/5.34.0/Log/Dispatch/Email/MailSend.pm
/usr/lib/perl5/vendor_perl/5.34.0/Log/Dispatch/Email/MailSender.pm
/usr/lib/perl5/vendor_perl/5.34.0/Log/Dispatch/Email/MailSendmail.pm
/usr/lib/perl5/vendor_perl/5.34.0/Log/Dispatch/File.pm
/usr/lib/perl5/vendor_perl/5.34.0/Log/Dispatch/File/Locked.pm
/usr/lib/perl5/vendor_perl/5.34.0/Log/Dispatch/Handle.pm
/usr/lib/perl5/vendor_perl/5.34.0/Log/Dispatch/Null.pm
/usr/lib/perl5/vendor_perl/5.34.0/Log/Dispatch/Output.pm
/usr/lib/perl5/vendor_perl/5.34.0/Log/Dispatch/Screen.pm
/usr/lib/perl5/vendor_perl/5.34.0/Log/Dispatch/Syslog.pm
/usr/lib/perl5/vendor_perl/5.34.0/Log/Dispatch/Types.pm
/usr/lib/perl5/vendor_perl/5.34.0/Log/Dispatch/Vars.pm
