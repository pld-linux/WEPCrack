%include	/usr/lib/rpm/macros.perl
Summary:	Tool that cracks 802.11 WEP encryption keys
Summary(pl.UTF-8):	Program do łamania szyfrowania WEP dla protokołu 802.11
Name:		WEPCrack
Version:	0.1.0
Release:	2
License:	GPL
Group:		Networking
Source0:	http://dl.sourceforge.net/wepcrack/%{name}-%{version}.tar.gz
# Source0-md5:	bbab3f07c8b47ac275459320f698711a
URL:		http://sourceforge.net/projects/wepcrack/
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WEPCrack is a tool that cracks 802.11 WEP encryption keys using the
latest discovered weakness of RC4 key scheduling.

%description -l pl.UTF-8
WEPCrack to program do łamania szyfrowania WEP dla protokołu 802.11,
przy użyciu luki znalezionej w kluczach RC4.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install pcap-getIV.pl WeakIVGen.pl WEPCrack.pl $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
