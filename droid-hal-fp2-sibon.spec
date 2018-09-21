# These and other macros are documented in dhd/droid-hal-device.inc
%define device FP2
%define vendor fairphone_devices

%define rpm_device fp2-sibon
%define rpm_vendor fairphone

%define installable_zip 1
%define enable_kernel_update 1

%define android_config \
#define QCOM_BSP 1\
#define DROID_AUDIO_HAL_ATOI_FIX 1\
%{nil}

%define makefstab_skip_entries /dev/cpuctl

%define straggler_files \
/init.class_main.sh\
/init.mdm.sh\
/init.qcom.class_core.sh\
/init.qcom.early_boot.sh\
/init.qcom.factory.sh\
/init.qcom.sh\
/init.qcom.ssr.sh\
/init.qcom.syspart_fixup.sh\
/init.qcom.usb.sh\
/selinux_version\
/service_contexts\
%{nil}

%define additional_post_scripts \
/usr/bin/groupadd-user media_rw || :\
%{nil}

%include rpm/dhd/droid-hal-device.inc
