%define git 20250707
Name:           labwc-tweaks-gtk
Version:        0.1.0~%{git}
Release:        1
Summary:        GUI Configuration app for labwc
License:        GPL-2.0-only
URL:            https://github.com/labwc/labwc-tweaks-gtk
Source:         https://github.com/labwc/labwc-tweaks-gtk/archive/refs/heads/labwc-tweaks-gtk-master.tar.gz
BuildRequires:  meson
BuildRequires:  gettext
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  cmake(VulkanHeaders)
Requires:       labwc

%description
labwc-tweaks is a GUI configuration application for the labwc Wayland compositor

%prep
%autosetup -n labwc-tweaks-gtk-master -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%license LICENSE
%{_bindir}/labwc-tweaks-gtk
%{_datadir}/applications/labwc-tweaks-gtk.desktop
%{_iconsdir}/hicolor/scalable/apps/labwc-tweaks-gtk.svg
