%define major 1
%define libname %mklibname seccomp %{major}
%define develname %mklibname -d seccomp

Summary:	Enhanced seccomp library
Name:		libseccomp
Version:	1.0.0
Release:	1
ExclusiveArch:	%{ix86} x86_64
License:	LGPLv2
Group:		System/Libraries
Source0:	http://downloads.sf.net/project/libseccomp/%{name}-%{version}.tar.gz
URL:		http://libseccomp.sourceforge.net
Requires:	kernel >= 3.5

%description
The libseccomp library provides an easy to use interface to the Linux Kernel's
syscall filtering mechanism, seccomp.  The libseccomp API allows an application
to specify which syscalls, and optionally which syscall arguments, the
application is allowed to execute, all of which are enforced by the Linux
Kernel.


%package -n     %{libname}
Summary:        Collection library providing GObject-based interfaces and classes
Group:          System/Libraries

%description -n %{libname}
The libseccomp library provides an easy to use interface to the Linux Kernel's
syscall filtering mechanism, seccomp.  The libseccomp API allows an application
to specify which syscalls, and optionally which syscall arguments, the
application is allowed to execute, all of which are enforced by the Linux
Kernel.

%package -n	%{develname}
Summary:	Development files used to build applications with libseccomp support
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	seccomp-devel = %{version}-%{release}

%description -n	%{develname}
The libseccomp library provides an easy to use interface to the Linux Kernel's
syscall filtering mechanism, seccomp.  The libseccomp API allows an application
to specify which syscalls, and optionally which syscall arguments, the
application is allowed to execute, all of which are enforced by the Linux
Kernel.

%prep
%setup -q

%build
%configure2_5x
%make

%install
mkdir -p "%{buildroot}/%{_libdir}"
mkdir -p "%{buildroot}/%{_includedir}"
mkdir -p "%{buildroot}/%{_mandir}"
%makeinstall_std

%files -n %{libname}
%{_libdir}/libseccomp.so.*

%files -n %{develname}
%doc LICENSE CREDITS README
%{_includedir}/seccomp.h
%{_libdir}/libseccomp.so
%{_libdir}/pkgconfig/libseccomp.pc
%{_mandir}/man3/*
