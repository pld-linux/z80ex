Summary:	ZiLOG Z80 CPU emulator
Name:		z80ex
Version:	1.1.21
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/z80ex/%{name}-%{version}.tar.gz
# Source0-md5:	92ab8d8f45fd7b448075b820013a5f97
URL:		http://z80ex.sourceforge.net/
BuildRequires:	cmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ZiLOG Z80 CPU emulator

Features:

- precise opcode emulation (documented & undocumented)
- exact timings for each opcode (including I/O operations)
- full support for all interrupt modes
- any number of virtual CPUs may be created
- portable: written in pure ANSI C
- builds as a library with simple callback-based API
- disassembler included

%package devel
Summary:	%{name} header files
Summary(pl.UTF-8):	Pliki nagłówkowe %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
z80ex header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe z80ex.

%package static
Summary:	Static %{name} libraries
Summary(pl.UTF-8):	Biblioteki statyczne %{name}
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static z80ex libraries.

%description static -l pl.UTF-8
Biblioteki statyczne z80ex.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	.. \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

install examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libz80ex.so.1
%attr(755,root,root) %{_libdir}/libz80ex.so.1.1.21
%attr(755,root,root) %ghost %{_libdir}/libz80ex_dasm.so.1
%attr(755,root,root) %{_libdir}/libz80ex_dasm.so.1.1.21

%files devel
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_libdir}/libz80ex.so
%attr(755,root,root) %{_libdir}/libz80ex_dasm.so
%{_examplesdir}/%{name}-%{version}
%{_includedir}/z80ex

%files static
%defattr(644,root,root,755)
%{_libdir}/libz80ex.a
%{_libdir}/libz80ex_dasm.a
