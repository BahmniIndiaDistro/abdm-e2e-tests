const path = require('path');
const axios = require('axios')
var _date = require("./date");
const assert = require("assert");

async function getOpenMRSResponse(request){
    return await axios.get(request
        , {
            headers: {
                'Authorization': `token ${process.env.receptionist}`
            }
        })
}

async function makeOpenVisitCall(patientUUID,visitType,URL){
    var yesterday = _date.getddmmyyyyFormattedDate(_date.yesterday())
    var tomorrow = _date.getddmmyyyyFormattedDate(_date.tomorrow())

    var request_URL = process.env.bahmniHost+URL
        .replace("<patientId>",patientUUID)
        .replace("<fromDate>",yesterday)
        .replace("<toDate>",tomorrow)
        .replace("<visitType>",visitType)

    console.log(request_URL)
    var prescriptionsVisitResponse = await getOpenMRSResponse(request_URL)

    assert.ok(prescriptionsVisitResponse.status==200)

    console.log(prescriptionsVisitResponse.data);
    console.log(prescriptionsVisitResponse.headers);
    console.log(prescriptionsVisitResponse.config);
    return prescriptionsVisitResponse.data;
}

async function makeOpenProgramCall(patientUUID,programName,programEnrollmentId,URL){
    var yesterday = _date.getddmmyyyyFormattedDate(_date.yesterday())
    var tomorrow = _date.getddmmyyyyFormattedDate(_date.tomorrow())

    var request_URL = process.env.bahmniHost+URL
        .replace("<patientId>",patientUUID)
        .replace("<fromDate>",yesterday)
        .replace("<toDate>",tomorrow)
        .replace("<programName>",programName)
        .replace("<programEnrollmentId>",programEnrollmentId)

    console.log(request_URL)
    var prescriptionsVisitResponse = await getOpenMRSResponse(request_URL)

    assert.ok(prescriptionsVisitResponse.status==200)

    console.log(prescriptionsVisitResponse.data);
    console.log(prescriptionsVisitResponse.headers);
    console.log(prescriptionsVisitResponse.config);
    return prescriptionsVisitResponse.data;
}

module.exports={
    getOpenMRSResponse:getOpenMRSResponse,
    makeOpenVisitCall:makeOpenVisitCall,
    makeOpenProgramCall:makeOpenProgramCall,
}