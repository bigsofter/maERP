import CoreGraphics
import Foundation
let list = CGWindowListCopyWindowInfo([.optionAll], kCGNullWindowID) as! [[String: Any]]
for w in list {
    let owner = w[kCGWindowOwnerName as String] as? String ?? ""
    if !owner.contains("1cv8") { continue }
    let b = w[kCGWindowBounds as String] as? [String: Any] ?? [:]
    print(w[kCGWindowNumber as String] ?? 0, w[kCGWindowOwnerPID as String] ?? 0, w[kCGWindowLayer as String] ?? 0,
          b["Width"] ?? 0, b["Height"] ?? 0, w[kCGWindowIsOnscreen as String] ?? 0, w[kCGWindowName as String] ?? "")
}
