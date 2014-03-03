Summary:	ZiLOG Z80 CPU emulator
Summary(pl.UTF-8):	Emulator procesora ZiLOG Z80
Name:		z80ex
Version:	1.1.21
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/z80ex/%{name}-%{version}.tar.gz
# Source0-md5:	92ab8d8f45fd7b448075b820013a5f97
URL:		http://z80ex.sourceforge.net/
BuildRequires:	cmake >= 2.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Z80Ex is a ZiLOG Z80 CPU emulator.

Features:
- precise opcode emulation (documented & undocumented)
- exact timings for each opcode (including I/O operations)
- full support for all interrupt modes
- any number of virtual CPUs may be created
- portable: written in pure ANSI C
- builds as a library with simple callback-based API
- disassembler included

%description -l pl.UTF-8
Z80Ex to emulator procesora ZiLOG Z80.

Możliwości:
- precyzyjna emulacja instrukcji (udokumentowanych i nie)
- dokładne czasy dla wszystkich instrukcji (wraz z operacjami we/wy)
- pełna obsługa wszystkich trybów przerwań
- możliwość utworzenia dowolnej liczby wirtualnych procesorów
- przenośność - napisany w czystym ANSI C
- budowanie jako biblioteka z prostym API opartym na wywołaniach
  zwrotnych
- dołączony disasembler

%package devel
Summary:	Z80Ex header files
Summary(pl.UTF-8):	Pliki nagłówkowe Z80Ex
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for Z80Ex libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek Z80Ex.

%package static
Summary:	Static Z80Ex libraries
Summary(pl.UTF-8):	Biblioteki statyczne Z80Ex
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Z80Ex libraries.

%description static -l pl.UTF-8
Biblioteki statyczne Z80Ex.

%prep
%setup -q

%build
install -d build
cd build
%cmake ..

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
%doc Changelog README TODO
%attr(755,root,root) %{_libdir}/libz80ex.so.1.1.21
%attr(755,root,root) %ghost %{_libdir}/libz80ex.so.1
%attr(755,root,root) %{_libdir}/libz80ex_dasm.so.1.1.21
%attr(755,root,root) %ghost %{_libdir}/libz80ex_dasm.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libz80ex.so
%attr(755,root,root) %{_libdir}/libz80ex_dasm.so
%{_includedir}/z80ex
%{_examplesdir}/%{name}-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libz80ex.a
%{_libdir}/libz80ex_dasm.a
