%define major 1

Name:		polkit-qt-1
Version:	0.112.0
Summary:	Library that allows developer to access PolicyKit-1 API
Release:	0.2
License:	LGPLv2+
Group:		Graphical desktop/KDE
URL:		https://projects.kde.org/projects/kdesupport/polkit-qt-1
Source0:	http://fr2.rpmfind.net/linux/KDE/stable/apps/KDE4.x/admin/%{name}-%{version}.tar.bz2

## upstream patches
Patch1: 0001-do-not-use-global-static-systembus-instance.patch
Patch2: 0002-fix-build-with-Qt4-which-doesn-t-have-QStringLiteral.patch
Patch3: 0003-Fix-QDBusArgument-assertion.patch
Patch5: 0005-Add-wrapper-for-polkit_system_bus_name_get_user_sync.patch
Patch6: 0006-Drop-use-of-deprecated-Qt-functions.patch
Patch7: 0007-Fix-compilation-with-Qt5.6.patch
Patch8: 0008-Allow-compilation-with-older-polkit-versions.patch
Patch9: polkit-qt-1-0.112.0-no_consolekit.patch

BuildRequires:	polkit-1-devel >= 0.98.1
BuildRequires:	qt4-devel
BuildRequires:	cmake
BuildRequires:	automoc4

%description
Polkit-qt is a library that allows developer to access PolicyKit-1
API with a nice Qt-style API

#-----------------------------------------------------------------------------
%define libpolkit_qt_core_1 %mklibname polkit-qt-core-1_ %{major}

%package -n %{libpolkit_qt_core_1}
Summary:	Polkit-Qt core library
Group:		System/Libraries
Obsoletes:	%{_lib}polkit-qt-core-10 < %{version}-%{release}

%description -n %{libpolkit_qt_core_1}
Polkit-Qt core library.

%files -n %{libpolkit_qt_core_1}
%{_libdir}/libpolkit-qt-core-1.so.%{major}*

#-----------------------------------------------------------------------------
%define libpolkit_qt_gui_1 %mklibname polkit-qt-gui-1_ %{major}

%package -n %{libpolkit_qt_gui_1}
Summary:	Polkit-Qt core library
Group:		System/Libraries
Obsoletes:	%{_lib}polkit-qt-gui-10 < %{version}-%{release}

%description -n %{libpolkit_qt_gui_1}
Polkit-Qt core library.

%files -n %{libpolkit_qt_gui_1}
%{_libdir}/libpolkit-qt-gui-1.so.%{major}*

#-----------------------------------------------------------------------------
%define libpolkit_qt_agent_1 %mklibname polkit-qt-agent-1_ %{major}

%package -n %{libpolkit_qt_agent_1}
Summary:	Polkit-Qt core library
Group:		System/Libraries
Obsoletes:	%{_lib}polkit-qt-agent-10 < %{version}-%{release}

%description -n %{libpolkit_qt_agent_1}
Polkit-Qt core library.

%files -n %{libpolkit_qt_agent_1}
%{_libdir}/libpolkit-qt-agent-1.so.%{major}*

#-----------------------------------------------------------------------------

%package   devel
Summary:	Devel stuff for polkit-Qt
Group:		Development/KDE and Qt
Requires:	%{libpolkit_qt_core_1} = %{version}-%{release}
Requires:	%{libpolkit_qt_gui_1} = %{version}-%{release}
Requires:	%{libpolkit_qt_agent_1} = %{version}-%{release}

%description  devel
This package contains header files needed if you wish to build applications
based on %{name}.

%files devel
%{_includedir}/polkit-qt-1
%{_libdir}/libpolkit-qt-agent-1.so
%{_libdir}/libpolkit-qt-core-1.so
%{_libdir}/libpolkit-qt-gui-1.so
%{_libdir}/pkgconfig/polkit-qt-1.pc
%{_libdir}/pkgconfig/polkit-qt-agent-1.pc
%{_libdir}/pkgconfig/polkit-qt-core-1.pc
%{_libdir}/pkgconfig/polkit-qt-gui-1.pc
%{_libdir}/cmake/PolkitQt-1/*.cmake

#-----------------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
%cmake_qt4 -DUSE_QT4=ON -DUSE_QT5=OFF
%make

%install
%makeinstall_std -C build

%changelog
* Thu Dec 15 2011 Alexander Khrukin <akhrukin@mandriva.org> 0.103.0-3
+ Revision: 741676
- version update 0.103.0

* Thu Dec 08 2011 Zé <ze@mandriva.org> 0.99.0-3
+ Revision: 738828
- clean defattr, BR, clena section and mkrel
- no need to have severall major defined
- rebuild

* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.99.0-2
+ Revision: 667802
- mass rebuild

  + Funda Wang <fwang@mandriva.org>
    - update url

* Fri Dec 10 2010 Funda Wang <fwang@mandriva.org> 0.99.0-1mdv2011.0
+ Revision: 620209
- new version 0.99.0
- update license
- update url

* Tue Oct 26 2010 Funda Wang <fwang@mandriva.org> 0.98.1-1mdv2011.0
+ Revision: 589417
- new snapshot for newer kdelibs4

* Sat Jul 31 2010 Funda Wang <fwang@mandriva.org> 0.96.1-1mdv2011.0
+ Revision: 563987
- new version 0.96.1

* Wed Dec 23 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.95.1-1mdv2010.1
+ Revision: 481756
- Fix release

* Wed Dec 23 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.95.1-0.1056463.1mdv2010.1
+ Revision: 481717
- Update to 0.9.5.1

* Mon Nov 30 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.95.0-0.1056463.1mdv2010.1
+ Revision: 471702
- Do not use kde4 macros
- import polkit-qt-1

