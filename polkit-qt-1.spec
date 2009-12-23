%define         svn  1056463

Name:           polkit-qt-1
Version:        0.95.1
Summary:        Library that allows developer to access PolicyKit-1 API
Release:        %mkrel 1
License:        GPL
Group:          Graphical desktop/KDE
URL:            http://www.kde.org/
Source0:        %{name}-%{version}.tar.bz2
BuildRoot:      %_tmppath/%name-%version-%release-buildroot
BuildRequires:  polkit-1-devel >= 0.95
BUildRequires:  qt4-devel
BuildRequires:  cmake
BuildRequires:  automoc4

%description
Polkit-qt is a library that allows developer to access PolicyKit-1
API with a nice Qt-style API

#-----------------------------------------------------------------------------

%define libpolkit_qt_core_1_major 0
%define libpolkit_qt_core_1 %mklibname polkit-qt-core-1 %{libpolkit_qt_core_1_major}

%package -n %libpolkit_qt_core_1
Summary: Polkit-Qt core library
Group: System/Libraries

%description -n %libpolkit_qt_core_1
Polkit-Qt core library.

%files -n %libpolkit_qt_core_1
%defattr(-,root,root)
%_libdir/libpolkit-qt-core-1.so.%{libpolkit_qt_core_1_major}*

#-----------------------------------------------------------------------------

%define libpolkit_qt_gui_1_major 0
%define libpolkit_qt_gui_1 %mklibname polkit-qt-gui-1 %{libpolkit_qt_gui_1_major}

%package -n %libpolkit_qt_gui_1
Summary: Polkit-Qt core library
Group: System/Libraries

%description -n %libpolkit_qt_gui_1
Polkit-Qt core library.

%files -n %libpolkit_qt_gui_1
%defattr(-,root,root)
%_libdir/libpolkit-qt-gui-1.so.%{libpolkit_qt_gui_1_major}*

#-----------------------------------------------------------------------------

%define libpolkit_qt_agent_1_major 0
%define libpolkit_qt_agent_1 %mklibname polkit-qt-agent-1 %{libpolkit_qt_agent_1_major}

%package -n %libpolkit_qt_agent_1
Summary: Polkit-Qt core library
Group: System/Libraries

%description -n %libpolkit_qt_agent_1
Polkit-Qt core library.

%files -n %libpolkit_qt_agent_1
%defattr(-,root,root)
%_libdir/libpolkit-qt-agent-1.so.%{libpolkit_qt_agent_1_major}*

#-----------------------------------------------------------------------------

%package   devel
Summary:   Devel stuff for polkit-Qt
Group:     Development/KDE and Qt
Requires:  %libpolkit_qt_core_1 = %version-%release
Requires:  %libpolkit_qt_gui_1 = %version-%release
Requires:  %libpolkit_qt_agent_1 = %version-%release
%description  devel
This package contains header files needed if you wish to build applications
based on %name.

%files devel
%defattr(-,root,root)
%{_includedir}/polkit-qt-1
%{_libdir}/libpolkit-qt-agent-1.so
%{_libdir}/libpolkit-qt-core-1.so
%{_libdir}/libpolkit-qt-gui-1.so
%{_libdir}/pkgconfig/polkit-qt-1.pc
%{_libdir}/pkgconfig/polkit-qt-agent-1.pc
%{_libdir}/pkgconfig/polkit-qt-core-1.pc
%{_libdir}/pkgconfig/polkit-qt-gui-1.pc

#-----------------------------------------------------------------------------

%prep
%setup -q -n %name-%version

%build

%cmake_qt4
%make


%install
rm -rf %buildroot
%makeinstall_std -C build

%clean
rm -rf %{buildroot}

