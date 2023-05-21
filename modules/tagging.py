# coding: utf-8

import oci

##########################################################################
# tag associated resources
##########################################################################


def tag_resources(type, oci_client, resource_id, defined_tags_dict):
    
    if type == 'compute':
        details = oci.core.models.UpdateInstanceDetails(defined_tags=defined_tags_dict)
        response = oci_client.update_instance(resource_id,details)

    if type == 'bootvolume':
        try:
            details = oci.core.models.UpdateBootVolumeDetails(defined_tags={})
            response = oci_client.update_boot_volume(resource_id,details)
        except:
            pass
        details = oci.core.models.UpdateBootVolumeDetails(defined_tags=defined_tags_dict)
        response = oci_client.update_boot_volume(resource_id,details)
        
    if type == 'volume':
        try:
            details = oci.core.models.UpdateVolumeDetails(defined_tags={})
            response = oci_client.update_volume(resource_id,details)
        except:
            pass
        details = oci.core.models.UpdateVolumeDetails(defined_tags=defined_tags_dict)
        response = oci_client.update_volume(resource_id,details)

    if type == 'boot_backup':
        try:
            details = oci.core.models.UpdateBootVolumeBackupDetails(defined_tags={})
            response = oci_client.update_boot_volume_backup(resource_id,details)
        except:
            pass
        details = oci.core.models.UpdateBootVolumeBackupDetails(defined_tags=defined_tags_dict)
        response = oci_client.update_boot_volume_backup(resource_id,details)

    if type == 'volume_backup':
        try:
            details = oci.core.models.UpdateVolumeBackupDetails(defined_tags={})
            response = oci_client.update_volume_backup(resource_id,details)
        except:
            pass
        details = oci.core.models.UpdateVolumeBackupDetails(defined_tags=defined_tags_dict)
        response = oci_client.update_volume_backup(resource_id,details)

 
    return response