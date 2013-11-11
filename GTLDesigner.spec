Summary:	Graphics Transfomation Languages Designer
Summary(pl.UTF-8):	Narzędzie do projektowania dla języków przekształceń graficznych GTL
Name:		GTLDesigner
Version:	0.9.2
Release:	2
License:	LGPL v2.1+
Group:		X11/Applications/Graphics
Source0:	http://download.opengtl.org/%{name}-%{version}.tar.bz2
# Source0-md5:	4a7457531e10831d4b41bc4d8a3ed1a6
Patch0:		%{name}-update.patch
URL:		http://opengtl.org/
BuildRequires:	QtCore-devel >= 4
BuildRequires:	QtGui-devel >= 4
BuildRequires:	OpenGTL-devel >= 0.9.3
BuildRequires:	cmake >= 2.6
BuildRequires:	kde4-kdelibs-devel >= 4
BuildRequires:	libQtGTL-devel >= 0.9.0
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= 4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Graphics Transfomation Languages Designer.

%description -l pl.UTF-8
Narzędzie do projektowania dla języków przekształceń graficznych GTL.

%prep
%setup -q
%patch0 -p1

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang gtldesigner --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f gtldesigner.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gtldesigner
%{_datadir}/apps/gtldesigner
%{_datadir}/config.kcfg/gtldesigner.kcfg
%{_desktopdir}/kde4/gtldesigner.desktop
%{_iconsdir}/hicolor/*x*/apps/gtldesigner.png
