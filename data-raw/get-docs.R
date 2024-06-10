# 10 June 24
# Extract Links to Evaluation Strategies and Output by Department

url <- "https://www.gov.uk/government/collections/evaluation-strategies-from-uk-government-departments"
req <- httr::GET(url)
body <- req |>
  httr::content()

links <- (body |>
  xml2::xml_find_all("//div[@class='responsive-bottom-margin']//a") |>
  xml2::xml_attr("href"))[-21]

links[4:20] <- paste0("https://www.gov.uk", links[4:20])


dept <- c("ONS", "FSA", "CPS", "MOD", "BEIS", "DFE", 
  "DFT", "DHSC", "DITS", "DLUHC", "DWP", 
  "FCDO", "HMRC", "DCMS", "HMT", "HO", 
  "MOJ", "CO", "DEFRA", "DESZN")

dplyr::tibble(dept, links) |>
  write.csv("data/meta.csv", row.names = FALSE)
