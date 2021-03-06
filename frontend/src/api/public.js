import handler from './apiHandler';

export const createIncident = async incidentData => {
    return (await handler.post(`/public/incidents/`, incidentData)).data;
}

export const updateIncident = async (incidentId, incidentData) => {
    return (await handler.put(`/public/incidents/${incidentId}`, incidentData)).data;
}

export const updateReporter = async (reporterId, reporterData) => {
    return (await handler.put(`/public/reporters/${reporterId}`, reporterData)).data;
}

// export const uploadFile = async (incidentId, formData) => {
//     return (await handler.post(`/public/incidents/${incidentId}/files`, formData)).data
// }

export const attachMedia = async (incidentId, mediaData) => {
    return (await handler.post(`/public/incidents/${incidentId}/attach_media`, mediaData)).data;
}

export const loadIncident = async (loadData) => {
    return (await handler.post(`/public/reporter/get_incident`, loadData)).data;
}

export const checkIncidentStatus = async (refId) => {
    return (await handler.get(`/public/incidents/?refId=`+refId)).data;
}

export const updateIncidentWorkflow = async (incidentId, workflowType, workflowUpdate) => {
    return (await handler.post(`/public/incidents/${incidentId}/workflow/${workflowType}`, workflowUpdate)).data;
};