# Robin-extremal research lines

This file holds the current mathematical questions suggested by the durable robin-extremal intuitions. It is not a roadmap, task queue, status page, or history.

## Price one-sided near-left cancellation by reciprocal-scale radius and compare it with the exterior budget

**Linked intuitions:** `MI-001-robin-failure-requires-self-tangent-half-mass-event-gaps` through `MI-030-scale-maximal-anchoring-converts-rightward-horizontal-advantage-into-an-exponential-shell-budget`.

RE-112--RE-138 reduce the attained finite-edge branch to a strong atom plus reciprocal-scale cancellation geometry. RE-139--RE-142 show that rightmost-anchored Turán visibility can lose an unusable transfer factor even under strong upper source envelopes. RE-143 removes that transfer by anchoring at the original algebraically strong atom and applying Turán's First Main Theorem only to zeros on or to its right.

RE-144 then closes the naive shrinking-slab hope: a matched simple spectrum can have a strong target with **exactly one** retained mode on or to its right, negligible far-left and high-height tails, and still hide the target on a fixed-relative observation window using a near-left cluster whose scaled radius `R(U)` tends to infinity as slowly as prescribed. The cluster may lie inside `o(log U/U)` width, and scaled radius only `O(log B)` already supports polynomial suppression in local cardinality `B`.

RE-145 adds the missing rate. For the positive empirical-measure representation underlying the Robin packet, every packet confined to scaled radius `R` has normalized local visibility at least `exp(-O_kappa(R))`, uniformly in cardinality and arrangement. This exponential dependence is the correct functional order in the matched class: the `RE-144` product packets attain exponential suppression in scaled radius after normalization. Hence `R(U)=o(log U)` still leaves a `U^{-o(1)}` local floor even though it does **not** restore a fixed positive floor and therefore still permits qualitative `o(M_0)` hiding.

RE-146 prices the first actual-zeta exterior piece in the same variable. If the anchor is chosen to maximize the leading Robin atom at scale `U`, then a rightward displacement `R/U` forces its coefficient ratio to be at most `e^{-R}` and therefore forces exponential ordinate inflation. On a fixed earlier subwindow this becomes a fractional coefficient moment, so a zero-density estimate gives a rightward-shell budget exponential in `R` relative to the anchor.

RE-147 replaces the original Ingham input by Pintz's high-sigma density theorem. If `delta=1-Theta<1/12`, the sufficient early-window tax drops from order `delta` to order `delta^(3/2)`:

\[
\kappa>
\tau_P(\delta)
=
\frac{3}{\sqrt2}\delta^{3/2}+9\delta^2.
\]

The same substitution improves the reciprocal-square high tail to exponent `-2+O(delta^(3/2))`. Thus global zero density is no longer the obvious quantitative bottleneck near `Theta=1`; the difficult geometry is local.

RE-148 removes the **location** part of the remaining synchronization issue. Exact dilation of the positive-measure theorem localizes the `RE-145` floor to every fixed nonempty early subwindow `[(1-kappa)U,(1-eta)U]`, so the local witness can be chosen at a point where the `RE-147` shell bound already holds uniformly. The resulting same-point comparison is

\[
\text{local packet}
\gtrsim
N_U e^{-C_{\kappa,\eta}R}
|a_{\rho_0}(u_*)|,
\qquad
\text{rightward shell}
\lesssim
U^D e^{-c_{\rm sh}R}
|a_{\rho_0}(u_*)|,
\]

with

\[
C_{\kappa,\eta}
=16(1-\eta)
\log\frac{2e(1-\eta)}{\kappa-\eta}
>19,
\qquad
0<c_{\rm sh}<\eta<\frac12.
\]

So the presently proved exponents are quantitatively incompatible: increasing one common reciprocal radius improves the shell estimate but degrades the guaranteed local floor much faster. The old question “can the visibility witness be forced into the early Pintz window?” is settled; the live question is whether the **local exponential constant** can be reduced enough using sharper positive-measure analysis or actual-zero geometry, or whether a stronger source-specific exterior estimate can outrun it.

The frontier is therefore a rate comparison with two additional unresolved geometries, not a location problem. One needs to improve the local-vs-right-shell exponent comparison while separately controlling the one-sided near-left cancellation of `RE-144` and modes that remain horizontally within `R/U` but are vertically remote from the anchor. A useful source theorem may attack any one of those three obligations, but merely enlarging a common reciprocal box, sharpening one-level sparsity, or shrinking an unscaled neighborhood is no longer a plausible closure mechanism.

## Keep target anchoring, radius loss, shell decay and unresolved exterior pieces separate

Target anchoring removes the rightmost-transfer loss, but it does not make the remaining left packet harmless. RE-144 shows that rightward count, far-left damping and high-height tails can all be benign while a growing near-left cluster carries the cancellation. RE-145 prices the local positive packet by scaled radius rather than cardinality. RE-146--RE-147 price the sufficiently-rightward actual-zeta shell by the same radius, with Pintz making the global-density tax cheap near the edge. RE-148 then puts those two estimates at the same observation point and shows that their **current exponential constants**, not their locations, fail to splice. Any closure should keep that rate mismatch distinct from the near-left and vertically remote pieces instead of folding all of them into “zero density” or “synchronization.”

## Keep the exact binary tie local

The surviving first/depth-two Four-Exponentials contingency remains local and does not control the finite-edge packet analysis. A global argument should remain robust to that binary alternative unless exact transcendence becomes load-bearing.