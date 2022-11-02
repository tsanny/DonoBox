function fillDeadline(deadline) {
  var month
  switch (deadline.substring(5, 7)) {
      case "01":
          month = "Januari"
          break
      case "02":
          month = "Februari"
          break
      case "03":
          month = "Maret"
          break
      case "04":
          month = "April"
          break
      case "05":
          month = "Mei"
          break
      case "06":
          month = "Juni"
          break
      case "07":
          month = "Juli"
          break
      case "08":
          month = "Agustus"
          break
      case "09":
          month = "September"
          break
      case "10":
          month = "Oktober"
          break
      case "11":
          month = "November"
          break
      case "12":
          month = "Desember"
          break
  }
  var result = "".concat(deadline.substring(8, 10), " ", month, " ", deadline.substring(0, 4))
  result = result.concat(" - ", deadline.substring(11, 19), " WIB")
  return result
}

function appendCrowdfund(id, title, fundraiser_name, collected, target, deadline) {
    $("#crowdfunds").append(`
      <div class="col-sm-6 col-md-4 p-3">
        <div class="card h-100">
          <div class="card-body">
            <h5 class="card-title">${title}</h5>
            <h6 class="card-subtitle text-muted">Digalang oleh ${fundraiser_name}</h6>
            <hr>
            <b>${collected}</b> terkumpul - <b>${target}</b> dibutuhkan
            <br>
            hingga <b>${fillDeadline(deadline)}</b>
            <br><br>
            <a href=${crowdfundUrl.replace("1", id)} class="btn border">Lihat Detail</a>
          </div>
        </div>
      </div>
    `)
}

$(document).ready(function() {
    $.get(ongoingUrl, function(crowdfunds) {
        if (crowdfunds.length != 0) {
            $("#no-crowdfunds").hide()
            for (const fund of crowdfunds) {
                appendCrowdfund(
                    fund["pk"],
                    fund["fields"]["title"],
                    fund["fields"]["fundraiser_name"],
                    fund["fields"]["collected"],
                    fund["fields"]["target"],
                    fund["fields"]["deadline"]
                )
            }
        }
    }, "json")
})