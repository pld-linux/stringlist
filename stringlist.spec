Summary:	Miscellaneous Memory and Configuration Function Library
Summary(pl):	Biblioteka funkcji konfiguracyjnych dla enlightenmenta
Name:		stringlist
Version:	0.3
Release:	2
Copyright:	GPL
Group:		Libraries
Group(pl):	Biblioteki
Source:		ftp://ftp.debian.org/debian/dists/main/devel/libs/%{name}-%{version}.tar.bz2
URL:		http://mandrake.net/
BuildRoot:	/tmp/%{name}-%{version}-root

%description
The StringList library provides several miscellaneous sets of functions
for tracking memory usage, Enlightenment's configuration language, file
and string manipulations.

%description -l pl 
Biblioteka StringList umo¿liwia ró¿norodne ustawienia funkcji 
konfiguracyjnych dla Enlightenmenta.

%package devel
Summary:	Header files and other resources for development
Summary(pl):	Pliki nag³ówkowe i inne zasoby potrzebne
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files and other resources for development stringlist based
applications.

%description -l pl devel
Pliki nagó³wkowe i inne zasoby potrzebne przy robieniu aplikacji
wykorzystujacych bibliotekê stringlist.

%package static
Summary:	Static stringlist library
Summary(pl):	Biblioteka statyczna stringlist
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static stringlist library.

%description -l pl static
Biblioteka statyczna stringlist.

%prep
%setup -q

%build
autoconf
LDFLAGS="-s"; export LDFLAGS
%configure \
	 --enable-shared \
	 --enable-static
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf ChangeLog NEWS README

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog.gz NEWS.gz README.gz
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*

%files static
%attr(644,root,root) %{_libdir}/lib*.a
