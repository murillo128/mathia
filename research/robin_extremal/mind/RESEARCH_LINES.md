# Robin-extremal research lines

This file records current mathematical questions for the Robin-extremal line. It is a mutable synthesis, not a task queue or history.

## Seek coefficient-phase interference outside same-ray serial single-center prediction

**Linked intuitions:** `MI-060-complex-single-center-drift-cannot-escape-a-fixed-prediction-corridor` and `MI-061-co-phased-serial-multicenter-has-no-wiener-discount`.

RE-229--RE-236 close the ordinary single-center escape routes far beyond the fixed-real regime. The local phase threshold, finite-ray prediction corridor and Wiener cost persist under complex drift; RE-236 removes the inverse-center proof artifact and shows that every contracting super-broad single-center family with bounded normalized Wiener rate forces an exponentially thin destination.

RE-237 tests the simplest proposed change of architecture: multiply several normalized single-center predictors. If all centers lie on one common complex ray, every factor has the same relative coefficient phase character. Convolution paths reaching a common output degree are therefore co-phased, so there is **no coefficient cancellation at all**:

`||prod_r F_r||_A = prod_r ||F_r||_A`.

The minimum delays add, and the normalized Wiener rate of the cascade is exactly the delay-weighted average of the constituent rates. A serial cascade of individually successful positive-real or same-ray predictors can never beat its best constituent merely by adding centers. In the delay-measure representation the same statement is exact multiplicativity of total variation under convolution.

The common-ray hypothesis is load-bearing. Different center phases can make convolution paths interfere, and RE-237 gives a finite algebraic example with strict Wiener submultiplicativity. Its rate conclusion also assumes the stages are individually successful predictors; a deliberately coupled product whose factors are not predictors is not covered.

The live multi-center frontier is therefore much more specific than “try several centers.” A useful architecture must make several centers contribute to the **same final coefficient with genuinely different phases before absolute values are taken**, or use parallel/additive/minimax synthesis, or arrange a coupled product whose predictive behavior exists only after composition. Those mechanisms must still beat the destination-width/Wiener-cost ledger left by the single-center results.

## Keep local flattening, destination width, coefficient phase and global Wiener cost distinct

The single-center results show that local flattening can be real while global cost destroys the gain. RE-237 adds a second representation trap: changing from one center to several centers does not change the cost mechanism if all coefficient paths remain locked to one phase character. Architectural multiplicity is not useful unless it creates an interference channel unavailable to the one-center representation.

Future candidates should therefore expose their final coefficient geometry before asymptotic optimization. If convolution paths are co-phased, Wiener cost multiplies exactly and serial composition cannot improve the normalized exponent. If phases differ, quantify the cancellation that survives DC normalization and the prediction constraint rather than relying on generic submultiplicativity. The remaining multi-center branch is an interference problem, not a center-count problem.

## Price phase-interfering products against the actual coupled Taylor remainder

RE-239--RE-240 distinguish two genuine effects outside the co-phased RE-237 class: nearby center phases give a quadratic Wiener discount at small separation, and a fixed small nonzero conjugate split can give an exponential coefficient-norm discount. Neither statement implies that the resulting product predicts on the observation arc. RE-241 finds an adverse first-order arc-edge Taylor cost against a second-order Wiener gain when each factor must separately pass its absolute-tail certificate; its refined constructive bound is `C_sep<5.9960`, not a universal lower bound.

Dropping factorwise certification does not remove the same local barrier automatically. RE-242 obtains the actual coupled conjugate-product error `Theta(m^(-1/2))` at its critical arc-edge threshold, with exponential failure below; RE-243 retains the obstruction as the pair coalesces at any rate. RE-244 gives the larger **DC-safe** fixed-multicenter geometric-tail normal form: at fixed arc phase `theta`, the product growth exponent is `F(theta)=sum_j s_j[tau_j(theta)]_+`. RE-245 removes the DC-safety restriction: the normalized exponent is `F(theta)-F(0)`, and its maximal exponential error exponent is `max_arc F-F(0)`. Even when this exponent is zero, positive logarithmic-potential rigidity proves that a DC-unsafe factor prevents uniform prediction. For these fixed finite Taylor products, prediction is therefore possible exactly when every constituent arc-edge exponent is nonpositive throughout the arc.

The remaining mathematical question is whether a construction outside this **fixed finite Taylor/geometric-tail regime** can couple error terms rather than only reduce coefficient norm—for example, a genuinely nongeometric remainder or a changing-number-of-factors limit—and simultaneously improve the destination-width/Wiener ledger. These results do not rule out such classes or prove a minimax bound for all predictors.

## Separate strict terminal rigidity from the sharp critical generalized-prime ambiguity

RE-238 proves that a quantitative Chebyshev remainder `|vartheta_Q(t)-t|<<t exp(-bV(t))`, with `V(t)=(log t)^(3/5)/(loglog t)^(1/5)`, forces the canonical terminal Robin source discrepancy to vanish for `b kappa_A>1/2`, `kappa_A=A^(3/5)(3/5)^(1/5)`. Its equality case is **not open**. RE-246 constructs generalized-prime source pairs agreeing exactly through `T=U_A(p)e^(-2)`, all obeying one uniform-in-source quantitative PNT bound at `b kappa_A=1/2`, while their normalized terminal Robin coordinates differ by arbitrary fixed signed amounts. This is source-information non-rigidity, not an ordinary-prime Robin counterexample.

RE-247 gives the full sharp result for an admissible moving horizon `U=U(p)`, `U/p->infinity`, and the *unit-constant* common source envelope `E_b(t)=t exp(-bV(t))`. Over pairs of discrete real-label generalized-prime sources agreeing below `T=e^(-2)U`, the supremal terminal ambiguity satisfies

`Delta_(p,b,U)=(2+o(1)) B_(p,b,U),  B_(p,b,U)=sqrt(p) log(p) exp(-bV(U))/log(U)`.

The `2` is the sharp asymptotic constant: discrete envelope-saturating source pairs attain it, not merely a signed formal measure. Therefore the source-class terminal ambiguity tends to zero **if and only if** `bV(U)-0.5log(p)+log(log(U)/log(p))->+infinity`. At the precise log-horizon transition `v=v_*(log p)+s v_*/log p`, its limit is `2 exp(-3s/10)`. The formal leading equality `b kappa_A=1/2` on the canonical horizon is already on the non-rigid side after the second-order correction. None of these comparisons imposes ordinary-prime source realization, a CA selector constraint, or a Robin sign conclusion.

The remaining source question is which *ordinary-prime and CA-selected* constraints forbid the generalized-prime envelope-saturating discrepancies, rather than attempting to recover rigidity from the quantitative PNT envelope alone. Real/integer-label separation and fixed congruences were stress-tested by RE-248--RE-251; they do not by themselves turn this generalized source-class result into an ordinary-prime assertion.

## Use the signed local prime-counting moment at the selected Robin horizon

RE-252 uses the pointwise Guth--Maynard short-interval input to extend the ordinary-prime local invisibility window, but its bound becomes only order one at `H_star=p^(3/4)(log p)^(-1/2) exp(0.5(log p)^(1/4))`. RE-253 identifies the exact unresolved *signed* statistic instead of treating a pointwise counting envelope as a cancellation theorem. For `L=log p` and ordinary-prime `N_p(y)=pi(p+y)-pi(p)`, set

`D_p(H)=int_0^H (N_p(y)-y/L)dy = sum_(p<q<=p+H)(H-(q-p))-H^2/(2L)`.

The direct Robin first-annulus integral obeys `sqrt(p)L int_p^(p+H)I(t)dt = -a_p D_p(H) + O(H(1+|vartheta(p)-p|)/p^(3/2) + LH^3/p^(5/2))`, with `a_p~L/p^(3/2)>0`. At regular self-tangent CA frontier primes, the already persisted endpoint bound gives `o(1)` for this first integral **if and only if** `D_p(H_star)=o(p^(3/2)/L)`; the pointwise input supplies only the corresponding `O` estimate. No sign or little-o is proved for that moment, and the remote annular contribution remains.

The new discriminating question is whether the CA selection condition gives a *signed triangular prime-counting cancellation* in precisely `D_p(H_star)`, together with the remaining remote-tail correlation. A theorem only about nonselected primes, or a bound on `|N_p(y)-y/L|` at each `y`, does not provide the needed selected-sign information.
