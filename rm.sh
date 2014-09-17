#!/bin/bash

# add the followng script into ~/.bashrc
# alias rm=PATH_TO_THIS_SCRIPT/rm.sh
# alias rmdir=PATH_TO_THIS_SCRIPT/rm.sh


TRASH_ROOT=/home/mazefeng/trash

for SOURCE_FULL_PATH in $@; do
    if [ "${SOURCE_FULL_PATH}" == "" ]; then echo "fail!"; fi
    if [ ! "${SOURCE_FULL_PATH:0:1}" == "/" ]; then SOURCE_FULL_PATH=`pwd`/${SOURCE_FULL_PATH}; fi
    SOURCE=`echo ${SOURCE_FULL_PATH} | awk -F '/' '{if ($NF=="") print $(NF-1); else print $NF}'`
    DATE=`date +%Y%m%d`
    TIMESTAMP=`date +%H%M%S`
    TRASH=${TRASH_ROOT}/${DATE}
    if [ ! -d ${TRASH} ]; then mkdir ${TRASH}; fi
    DEST=${TRASH}/${SOURCE}.${TIMESTAMP}
    mv ${SOURCE_FULL_PATH} ${DEST}
    LOG="[`date`]: ${SOURCE_FULL_PATH} --> ${DEST}"
    echo ${LOG} >> ${TRASH_ROOT}/log
    echo ${LOG}
done

exit 0

