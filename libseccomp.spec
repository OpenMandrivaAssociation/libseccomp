%define major	2
%define libname	%mklibname seccomp %{major}
%define devname	%mklibname -d seccomp

Summary:	Enhanced seccomp library
Name:		libseccomp
Version:	2.1.0
Release:	2
License:	LGPLv2
Group:		System/Libraries
Url:		http://libseccomp.sourceforge.net
Source0:	http://downloads.sf.net/project/libseccomp/%{name}-%{version}.tar.gz
ExclusiveArch:	%{ix86} x86_64 %arm
Requires:	kernel >= 3.5
%ifarch %arm
Requires:	kernel >= 3.8
%endif

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

%package -n	%{devname}
Summary:	Development files used to build applications with libseccomp support
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	seccomp-devel = %{version}-%{release}

%description -n	%{devname}
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
%{_libdir}/libseccomp.so.%{major}*

%files -n %{devname}
%doc LICENSE CREDITS README
%{_bindir}/scmp_sys_resolver
%{_includedir}/seccomp.h
%{_libdir}/libseccomp.so
%{_libdir}/pkgconfig/libseccomp.pc
%{_mandir}/man3/*
%{_mandir}/man1/*
