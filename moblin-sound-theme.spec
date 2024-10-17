Name: moblin-sound-theme
Version: 0.3
Release: %mkrel 3
Summary: Moblin sound theme
Group: System/X11
Source0: http://git.moblin.org/cgit.cgi/%{name}/snapshot/%{name}-%{version}.tar.bz2
License: GPLv2+ and LGPLv2+ and CC-BY-SA and CC-BY
Url: https://www.moblin.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: gettext
BuildRequires: intltool >= 0.40
Requires(post): coreutils
Requires(postun): coreutils

%description
Moblin sound theme


%prep
%setup -q

%build
autoreconf -fi
%configure

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%post
/bin/touch --no-create %{_datadir}/sounds/moblin %{_datadir}/sounds

%postun
/bin/touch --no-create %{_datadir}/sounds/moblin %{_datadir}/sounds

%files
%defattr(-,root,root)
%doc README
%dir %{_datadir}/sounds/moblin
%dir %{_datadir}/sounds/moblin/stereo
%{_datadir}/sounds/moblin/index.theme
%{_datadir}/sounds/moblin/stereo/*.ogg
%{_datadir}/sounds/moblin/stereo/*.wav


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3-3mdv2011.0
+ Revision: 620385
- the mass rebuild of 2010.0 packages

* Sun Oct 11 2009 Olivier Blin <oblin@mandriva.com> 0.3-2mdv2010.0
+ Revision: 456610
- require coreutils instead of file /bin/touch

* Wed Sep 30 2009 Olivier Blin <oblin@mandriva.com> 0.3-1mdv2010.0
+ Revision: 451503
- fix group
- use make macro
- initial import (from Claudio Matsuoka and Caio Begotti, based on Fedora package)
- Created package structure for moblin-sound-theme.

