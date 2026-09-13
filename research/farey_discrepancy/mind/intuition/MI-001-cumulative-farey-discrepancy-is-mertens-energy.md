# MI-001 — Natural frontier normalization removes predecessor entropy, but recursive eligibility remains open

**Evidence level:** supported by the exact physical occupation reductions through FD-084, the matched geometric control FD-085, the divisor-supported transport inequality FD-086, the exact dilation/terminal-sector bounds FD-087, the repeated-prime deflation construction FD-088, the canonical predecessor compression FD-089, and the prime-weighted frontier normalization FD-090. No theorem yet gives recursively iterable fixed-strength multiplicative transport.

FD-071--FD-084 show that every sufficiently late fixed-power future window contains a constant-strength occupied block of length `L_H=H^(Theta-delta)`. FD-085 proves that abundance and even linear additive blocks do not by themselves imply a bounded-ratio integer chain, while FD-086 shows that the complete physical Jordan vectors are projectively coherent throughout each such block.

FD-087 tests exact inter-block transport and separates two issues. Integer dilation is uniformly well conditioned, so exact copies themselves are not information-destroying. But every exact copy forced from an anchor `a<=L_H` lies in the terminal quotient sector, and the normalized energy of the entire sector tends to zero. Small common anchors therefore cannot transport the bulk frontier packet.

FD-088 escapes that capacity obstruction: a fixed positive share of the nonsquarefree frontier energy can be stitched with vanishing Hilbert distortion and represented by exact unit-weight lower anchors `a_r >> sqrt(H L_H) >> L_H`. FD-089 then compresses the row-dependent anchors to canonical prime contractions `A_p=ceil(H/p)` and shows that a subpower predecessor family already contains a lower state with the full frontier exponent.

FD-090 identifies the correct normalization of that family. If `M_(p,H)` is the actual transported mask energy, then for every `sigma>1/2`

`max_p M_(p,H)/A_p^(2 sigma) >= (c_(sigma,eta)-o(1)) E_(H,1)/H^(2 sigma)`.

The factor `A_p/H~1/p` turns the candidate family into the summable prime weight `p^(-2 sigma)`. Under false RH, setting `sigma=Theta` gives a **fixed-strength bound in frontier-normalized energy** for some canonical predecessor even when `alpha` is fixed. The `H^alpha` predecessor count therefore contributes no additional asymptotic entropy once the physical scale change is priced first. Diagonalizing `alpha->0` is needed only if one insists that the selected lower horizon remain `H^(1-o(1))`.

What remains is not predecessor cardinality. The selected mask may still be only a vanishing fraction of `E_(A_p,1)`, the lower state need not inherit positive nonsquarefree occupation, and in parent-scale units the unavoidable contraction cost is `p^(-2Theta)`. Thus a frontier-exponent recurrence is weaker than a recursively eligible source recurrence. The next theorem must propagate the occupation/mask condition needed to reuse the construction, or prove a composition law that consumes frontier-normalized carriers without requiring a fixed raw overlap.

**Boundary.** FD-090 is conditional on the false-RH frontier setup and does not produce an inter-block multiplicative chain, contradiction, or RH proof. Equal frontier exponents do not imply a fixed mask fraction, and the prime-weighted argument is fixed-strength only after the natural lower-scale normalization.