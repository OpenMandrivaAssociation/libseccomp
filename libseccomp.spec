%define major 2
%define libname %mklibname seccomp %{major}
%define devname %mklibname -d seccomp

Summary:	Enhanced seccomp library
Name:		libseccomp
Version:	2.6.0
Release:	2
License:	LGPLv2
Group:		System/Libraries
Url:		https://github.com/seccomp/libseccomp
Source0:	https://github.com/seccomp/libseccomp/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool-base
BuildRequires:	slibtool
BuildRequires:	make
BuildRequires:	kernel-release-headers
BuildRequires:	gperf
Requires:	kernel

%description
The libseccomp library provides an easy to use interface to the Linux Kernel's
syscall filtering mechanism, seccomp.  The libseccomp API allows an application
to specify which syscalls, and optionally which syscall arguments, the
application is allowed to execute, all of which are enforced by the Linux
Kernel.

%package -n %{libname}
Summary:	Collection library providing GObject-based interfaces and classes
Group:		System/Libraries

%description -n %{libname}
The libseccomp library provides an easy to use interface to the Linux Kernel's
syscall filtering mechanism, seccomp.  The libseccomp API allows an application
to specify which syscalls, and optionally which syscall arguments, the
application is allowed to execute, all of which are enforced by the Linux
Kernel.

%package -n %{libname}-static
Summary:	Collection library providing GObject-based interfaces and classes 
Group:		System/Libraries

%description -n %{libname}-static
Static version of libseccomp provides an easy to use interface to the Linux Kernel's
syscall filtering mechanism, seccomp.  The libseccomp API allows an application
to specify which syscalls, and optionally which syscall arguments, the
application is allowed to execute, all of which are enforced by the Linux
Kernel. This is a require of snapd confine


%package -n %{devname}
Summary:	Development files used to build applications with libseccomp support
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	seccomp-devel = %{EVRD}

%description -n	%{devname}
The libseccomp library provides an easy to use interface to the Linux Kernel's
syscall filtering mechanism, seccomp.  The libseccomp API allows an application
to specify which syscalls, and optionally which syscall arguments, the
application is allowed to execute, all of which are enforced by the Linux
Kernel.

%prep
%autosetup -p1

%build
%configure --enable-static
%make_build

%install
mkdir -p "%{buildroot}/%{_libdir}"
mkdir -p "%{buildroot}/%{_includedir}"
mkdir -p "%{buildroot}/%{_mandir}"
%make_install

%files -n %{libname}
%{_libdir}/libseccomp.so.%{major}*

%files -n %{libname}-static
%{_libdir}/libseccomp.a

%files -n %{devname}
%doc LICENSE CREDITS
%{_bindir}/scmp_sys_resolver
%{_includedir}/*.h
%{_libdir}/libseccomp.so
%{_libdir}/pkgconfig/libseccomp.pc
%doc %{_mandir}/man3/*
%doc %{_mandir}/man1/*
