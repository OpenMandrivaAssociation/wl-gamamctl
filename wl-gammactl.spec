
%global commit 07fc9fe9428301105863fd3a5844f92f2a87f33b
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global bumpver 1

%global s1commit c11408942e2fb54d41dadb84cdf844331076ae11
%global s1shortcommit %(c=%{s1commit}; echo ${c:0:7})
%global s1name wlr-protocols

Name:		wl-gammactl
Version:    1~%{bumpver}.git%{shortcommit}
Release:	1
Source0:	https://github.com/mischw/wl-gammactl/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:    https://github.com/swaywm/wlr-protocols/archive/%{s1commit}/%{s1name}-%{s1shortcommit}.tar.gz
Summary:    Small GTK GUI application to set contrast, brightness and gamma for wayland compositors which support the wlr-gamma-control protocol extension
URL:		https://github.com/mischw/wl-gammactl
License:	MIT
Group:      Windoe Manager/Utility

BuildSystem:	meson

BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(wlroots)
BuildRequires: pkgconfig(wayland-scanner)
%description
%summary.

%prep
%autosetup -n %{name}-%{commit} -p1
tar -xf %{S:1} -C wlr-protocols --strip-components=1

%files
%{_bindir}/%{name}
