Summary:	Miscellaneous Memory and Configuration Function Library
Summary(pl):	Biblioteka funkcji konfiguracyjnych dla enlightenmenta
Name:		stringlist
Version:	0.3
Release:	1d
Copyright:	GPL
Group:		X11/Libraries
Group(pl):	X11/Biblioteki
#######		ftp://ftp.debian.org/debian/dists/main/devel/libs
Source:		%{name}-%{version}.tar.bz2
URL:		http://mandrake.net/
BuildRoot:	/tmp/%{name}-%{version}-root

%description
The StringList library provides several miscellaneous sets of functions
for tracking memory usage, Enlightenment's configuration language, file
and string manipulations.

%description -l pl 
Biblioteka StringList umo¿liwia ró¿norodne ustawienia funkcji 
konfiguracyjnych dla Enlightenmenta.
 
%prep
%setup -q

%build
autoconf
CFLAGS=$RPM_OPT_FLAGS LDFLAGS=-s \
     ./configure %{_target} \
         --prefix=/usr/X11R6 \
	 --enable-shared \
	 --disable-static
make

%install
rm -rf $RPM_BUILD_ROOT

make prefix=$RPM_BUILD_ROOT/usr/X11R6 install

strip $RPM_BUILD_ROOT/usr/X11R6/lib/lib*.so.*.*

bzip2 -9 ChangeLog NEWS README

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog.bz2 NEWS.bz2 README.bz2

%attr(755,root,root) /usr/X11R6/lib/lib*.so*
/usr/X11R6/include/*

%changelog
* Fri Feb 05 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [0.3-1d]
- build for PLD,
- rewrote spec file.

* Tue Aug 18 1998 Term <term@dfw.net>
- First try at an RPM for StringList, hacked from esound's. :)
