#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Log-Dispatch
Version  : 2.68
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Log-Dispatch-2.68.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Log-Dispatch-2.68.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libl/liblog-dispatch-perl/liblog-dispatch-perl_2.67-1.debian.tar.xz
Summary  : 'Dispatches messages to one or more outputs'
Group    : Development/Tools
License  : Artistic-2.0 GPL-2.0 MIT
Requires: perl-Log-Dispatch-license
BuildRequires : buildreq-cpan
BuildRequires : perl(B::Hooks::EndOfScope)
BuildRequires : perl(Class::Data::Inheritable)
BuildRequires : perl(Devel::GlobalDestruction)
BuildRequires : perl(Dist::CheckConflicts)
BuildRequires : perl(Exception::Class)
BuildRequires : perl(Module::Implementation)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Package::Stash)
BuildRequires : perl(Params::ValidationCompiler)
BuildRequires : perl(Specio)
BuildRequires : perl(Specio::Declare)
BuildRequires : perl(Specio::Exporter)
BuildRequires : perl(Specio::Library::Builtins)
BuildRequires : perl(Specio::Library::Numeric)
BuildRequires : perl(Specio::Library::String)
BuildRequires : perl(Sub::Exporter::Progressive)
BuildRequires : perl(Sub::Identify)
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Test::Needs)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(Variable::Magic)
BuildRequires : perl(namespace::autoclean)
BuildRequires : perl(namespace::clean)

%description
# NAME
Log::Dispatch - Dispatches messages to one or more outputs
# VERSION
version 2.68

%package dev
Summary: dev components for the perl-Log-Dispatch package.
Group: Development
Provides: perl-Log-Dispatch-devel

%description dev
dev components for the perl-Log-Dispatch package.


%package license
Summary: license components for the perl-Log-Dispatch package.
Group: Default

%description license
license components for the perl-Log-Dispatch package.


%prep
%setup -q -n Log-Dispatch-2.68
cd ..
%setup -q -T -D -n Log-Dispatch-2.68 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Log-Dispatch-2.68/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/perl-Log-Dispatch
cp LICENSE %{buildroot}/usr/share/doc/perl-Log-Dispatch/LICENSE
cp deblicense/copyright %{buildroot}/usr/share/doc/perl-Log-Dispatch/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/Log/Dispatch.pm
/usr/lib/perl5/site_perl/5.26.1/Log/Dispatch/ApacheLog.pm
/usr/lib/perl5/site_perl/5.26.1/Log/Dispatch/Base.pm
/usr/lib/perl5/site_perl/5.26.1/Log/Dispatch/Code.pm
/usr/lib/perl5/site_perl/5.26.1/Log/Dispatch/Conflicts.pm
/usr/lib/perl5/site_perl/5.26.1/Log/Dispatch/Email.pm
/usr/lib/perl5/site_perl/5.26.1/Log/Dispatch/Email/MIMELite.pm
/usr/lib/perl5/site_perl/5.26.1/Log/Dispatch/Email/MailSend.pm
/usr/lib/perl5/site_perl/5.26.1/Log/Dispatch/Email/MailSender.pm
/usr/lib/perl5/site_perl/5.26.1/Log/Dispatch/Email/MailSendmail.pm
/usr/lib/perl5/site_perl/5.26.1/Log/Dispatch/File.pm
/usr/lib/perl5/site_perl/5.26.1/Log/Dispatch/File/Locked.pm
/usr/lib/perl5/site_perl/5.26.1/Log/Dispatch/Handle.pm
/usr/lib/perl5/site_perl/5.26.1/Log/Dispatch/Null.pm
/usr/lib/perl5/site_perl/5.26.1/Log/Dispatch/Output.pm
/usr/lib/perl5/site_perl/5.26.1/Log/Dispatch/Screen.pm
/usr/lib/perl5/site_perl/5.26.1/Log/Dispatch/Syslog.pm
/usr/lib/perl5/site_perl/5.26.1/Log/Dispatch/Types.pm
/usr/lib/perl5/site_perl/5.26.1/Log/Dispatch/Vars.pm

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
%defattr(-,root,root,-)
/usr/share/doc/perl-Log-Dispatch/LICENSE
/usr/share/doc/perl-Log-Dispatch/deblicense_copyright
