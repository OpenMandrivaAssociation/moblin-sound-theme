Name: moblin-sound-theme
Version: 0.3
Release: %mkrel 1
Summary: Moblin sound theme
Group: User Interface/Desktops
Source0: http://git.moblin.org/cgit.cgi/%{name}/snapshot/%{name}-%{version}.tar.bz2
License: GPLv2+ and LGPLv2+ and CC-BY-SA and CC-BY
Url: http://www.moblin.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: gettext
BuildRequires: intltool >= 0.40
Requires(post): /bin/touch
Requires(postun): /bin/touch

%description
Moblin sound theme


%prep
%setup -q

%build
autoreconf -fi
%configure

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

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