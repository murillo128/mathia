# MI-023 — Negative-witness collapse trades rowwise simplicity for source depth

**Evidence level:** proved for the flat Christoffel source by [MC-273](../../findings/MC-273-christoffel-negative-witness-homogeneous-collapse.md) and [MC-274](../../findings/MC-274-negative-witness-conditioning-fourier-depth-tax.md). No atom-scale witness-search theorem or endpoint cancellation estimate is claimed.

MC-273 gives an exact rowwise simplification. If a target sign vector has at least one negative lower-prime coordinate, then choosing any negative witness converts the mixed Hamming-ball coefficient

`g_m(x)=sum_(|S|<=m) x_S`

into the homogeneous degree-`m` shell on the remaining coordinates. Equivalently, `sum_(s<=m) K_s(b;k)=K_m(b-1;k-1)`. Every nonblind row therefore has amplitude at most `C(k-1,m)`, while the blind row has amplitude `Z_(k,m)=sum_(s<=m) C(k,s)`.

The simplification does not automatically globalize. MC-274 conditions on a witness through a deterministic coordinate-query tree and computes the exact Walsh/source degree of the conditioned energy. A leaf found after `j` queries has

`deg_W(I_j g_m^2)=2m+j`,

and recombining all witness leaves through depth `J` still gives degree `2m+J`. The extra depth is not an artifact of treating leaves separately: exact conditioning has inserted `J` additional lower-prime source coordinates into the observable.

There is also a cardinality tax. If `C` target rows are compared with independent signs, a depth-`J` witness search leaves natural unresolved mass `C 2^(-J)`. Eliminating every unresolved row by such atomwise conditioning requires roughly `J>log_2 C` (up to the allowed loss), which at the live Christoffel scale is of order `log y log log y`, far larger than the original detector depth `m=O(log log y)`.

So MC-273 does not turn the endpoint into an easy homogeneous-shell bound. It identifies a useful **conditional normal form**, while MC-274 shows that discovering the conditioning atom by atom can spend more source complexity than the original problem. A viable use of the collapse must therefore find the negative-witness information collectively, average it without resolving every row, or exploit a source identity that supplies the witness partition at much lower effective Fourier depth.

**Boundary.** The Fourier-depth tax applies to exact coordinate-query conditioning and the atom-scale elimination argument. It does not rule out a different aggregate certificate of nonblindness, a phase-sensitive averaging identity, or another source-specific mechanism that uses the MC-273 collapse without materializing every witness leaf.