#!/bin/bash

# 数据盘fio压测
# 随机读写混合测试（50%写）
# $fio_file -thread -filename="$DEVICE" -runtime=$RUNTIME -group_reporting -bs=$BS -direct=1 -rw=randrw -rwmixwrite=50 -ioengine="$engine" -numjobs="$NUMJOBS" -iodepth=$IODEPTH -name=fiotest01 >>"$host"_direct_randrw_"$diskname"
for i in $(nvme list|awk 'NR>2{print $1}');do
    DEVICE=$(echo "$i" | awk -F '/' '{print $3}')
    fio -thread -filename=$i -runtime=60 -group_reporting -bs=4K -direct=1 -rw=randread -ioengine=psync -numjobs=48 -iodepth=1 -name=fiotest01 > /tmp/4k_direct_randread_"$DEVICE"
    # 取压测数据中的平均带宽值
    data_avg_speed=$(awk '/READ/{print $3}' /tmp/4k_direct_randread_"$DEVICE" | tr -d '(),' )
    IOPS=$(awk '/read:/{print $2}' /tmp/4k_direct_randread_"$DEVICE" | tr -d ',')
    MS=$(awk '/^\s*lat \(usec\):/{print $5}' /tmp/4k_direct_randread_"$DEVICE" | tr -d ',')
    echo -e "$(date +"[%F %T]") $i 4k平均读取速率为：$data_avg_speed"
    echo -e "$(date +"[%F %T]") $i 4k平均IOPS为：$IOPS"
    echo -e "$(date +"[%F %T]") $i 4k平均延迟为：$MS us"
    echo -e "\033[33m$(date +"[%F %T]") $i 压测完成...\n\033[0m"
done
for i in $(nvme list|awk 'NR>2{print $1}');do
    DEVICE=$(echo "$i" | awk -F '/' '{print $3}')
    fio -thread -filename=$i -runtime=60 -group_reporting -bs=64K -direct=1 -rw=randread -ioengine=psync -numjobs=48 -iodepth=1 -name=fiotest01 > /tmp/64k_direct_randread_"$DEVICE"
    # 取压测数据中的平均带宽值
    data_avg_speed=$(awk '/READ/{print $3}' /tmp/64k_direct_randread_"$DEVICE" | tr -d '(),' )
    IOPS=$(awk '/read:/{print $2}' /tmp/64k_direct_randread_"$DEVICE" | tr -d ',')
    MS=$(awk '/^\s*lat \(usec\):/{print $5}' /tmp/64k_direct_randread_"$DEVICE" | tr -d ',')
    echo -e "$(date +"[%F %T]") $i 64k平均读取速率为：$data_avg_speed"
    echo -e "$(date +"[%F %T]") $i 64k平均IOPS为：$IOPS"
    echo -e "$(date +"[%F %T]") $i 64k平均延迟为：$MS us"
    echo -e "\033[33m$(date +"[%F %T]") $i 压测完成...\n\033[0m"
done

for i in $(nvme list|awk 'NR>2{print $1}');do
    DEVICE=$(echo "$i" | awk -F '/' '{print $3}')
    fio -thread -filename=$i -runtime=60 -group_reporting -bs=64K -direct=1 -rw=randwrite -ioengine=psync -numjobs=48 -iodepth=1 -name=fiotest01 > /tmp/64k_direct_randwrite_"$DEVICE"
    # 取压测数据中的平均带宽值
    data_avg_speed=$(awk '/WRITE/{print $3}' /tmp/64k_direct_randwrite_"$DEVICE" | tr -d '(),' )
    IOPS=$(awk '/write:/{print $2}' /tmp/64k_direct_randwrite_"$DEVICE" | tr -d ',')
    MS=$(awk '/^\s*lat \(usec\):/{print $5}' /tmp/64k_direct_randwrite_"$DEVICE" | tr -d ',')
    echo -e "$(date +"[%F %T]") $i 64k平均写入速率为：$data_avg_speed"
    echo -e "$(date +"[%F %T]") $i 64k平均IOPS为：$IOPS"
    echo -e "$(date +"[%F %T]") $i 64k平均延迟为：$MS us"
    echo -e "\033[33m$(date +"[%F %T]") $i 压测完成...\n\033[0m"
done
for i in $(nvme list|awk 'NR>2{print $1}');do
    DEVICE=$(echo "$i" | awk -F '/' '{print $3}')
    fio -thread -filename=$i -runtime=60 -group_reporting -bs=4K -direct=1 -rw=randwrite -ioengine=psync -numjobs=48 -iodepth=1 -name=fiotest01 > /tmp/4k_direct_randwrite_"$DEVICE"
    # 取压测数据中的平均带宽值
    data_avg_speed=$(awk '/WRITE/{print $3}' /tmp/4k_direct_randwrite_"$DEVICE" | tr -d '(),' )
    IOPS=$(awk '/write:/{print $2}' /tmp/4k_direct_randwrite_"$DEVICE" | tr -d ',')
    MS=$(awk '/^\s*lat \(usec\):/{print $5}' /tmp/4k_direct_randwrite_"$DEVICE" | tr -d ',')
    echo -e "$(date +"[%F %T]") $i 4k平均写入速率为：$data_avg_speed"
    echo -e "$(date +"[%F %T]") $i 4k平均IOPS为：$IOPS"
    echo -e "$(date +"[%F %T]") $i 4k平均延迟为：$MS us"
    echo -e "\033[33m$(date +"[%F %T]") $i 压测完成...\n\033[0m"
done
