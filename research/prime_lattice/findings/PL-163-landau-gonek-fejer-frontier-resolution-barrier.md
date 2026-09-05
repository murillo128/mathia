# PL-163 — Landau–Gonek moments couple horizontal zero displacement to prime phase, but the positive Fejér route loses frontier resolution

## Claim

The most direct weighted repair suggested by `PL-162` is already classical at the moment level and has a sharp resolution obstruction when one insists on positivity.

Fix a rational prime `p`, write a nontrivial zero as `rho=beta+i gamma`, and set

`y_rho=(beta-1/2) log p`,  `theta_rho=gamma log p (mod 2 pi)`.

For every integer `k>=1`, Gonek's uniform Landau formula applied at the prime power `x=p^k` controls the exact joint horizontal/vertical moment

`S_k(T)=sum_(0<gamma<=T) p^(k rho)`.

After reflection by the functional equation,

`Re(p^(-k/2) S_k(T))`
` = sum_(0<gamma<=T) cosh(k y_rho) cos(k theta_rho)`.

Thus the horizontal weight `p^(k(beta-1/2))` and the prime-torus phase `p^(i k gamma)` are not a new candidate coupling: they are precisely the classical Landau--Gonek channel.

There is a canonical positive way to combine these moments. Put `A=(log p)/2`, the half-width corresponding to the full critical strip `0<=beta<=1`, and for `K>=2` define

`H_(p,K)(y,theta)`
` = 1 + 2 sum_(1<=k<K) (1-k/K)`
`       [cosh(k y)/cosh(k A)] cos(k theta)`.

This function is nonnegative on the whole periodic strip `|y|<=A`: it is harmonic in `(y,theta)` and on both boundary components it is the ordinary nonnegative Fejer kernel. Consequently

`Z_(p,K)(T)=sum_(0<gamma<=T) H_(p,K)(y_rho,theta_rho) >= 0`

and there is the exact identity

`Z_(p,K)(T)`
` = N(T) + 4 sum_(1<=k<K) (1-k/K)`
`               Re S_k(T)/(p^k+1)`.

Gonek's integer uniform estimate

`S_k(T)`
` = -(T/(2 pi)) log p`
`   + O(p^k log(2 p^k T) log log(3 p^k))`

therefore yields

`Z_(p,K)(T)`
` = N(T)`
`   -(2 T log p/pi) sum_(1<=k<K) (1-k/K)/(p^k+1)`
`   + O_p(K (log T+K) log log(3 p^K T))`,

with harmless changes in the logarithmic factors depending on the chosen standard statement of Gonek's uniform theorem.

The same calculation exposes the obstruction. Full-strip positivity keeps the Landau--Gonek errors under polynomial control because the denominator `cosh(kA)` cancels the `p^(k/2)` growth after critical normalization, but it also damps all Fourier modes exponentially away from the trivial strip edge. If a hypothetical rightmost zero abscissa satisfies `Theta<1` and `B=(Theta-1/2)log p`, then for `|y|<=B`

`cosh(k y)/cosh(k A) << p^(-k(1-Theta))`.

Hence `H_(p,K)` is uniformly bounded on the entire hypothetical zero strip independently of `K`; increasing the Fejer degree cannot amplify a sparse phase-pinned near-frontier zero without bound.

If instead one builds the same positive harmonic Fejer kernel on the narrower strip `|y|<=B`, then a phase-pinned frontier zero has boundary response `K`, but the coefficient of the `k`th Landau--Gonek error becomes

`p^(k/2)/cosh(kB) asymp p^(k(1-Theta))`.

For every `Theta<1` this grows exponentially with the desired phase resolution. The published uniform Landau--Gonek estimate therefore loses control exactly when the positive kernel is narrowed from the trivial strip boundary to a hypothetical off-critical frontier.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + PRIOR-ART-REDIRECT + NEGATIVE/OBSTRUCTION`. The Landau--Gonek moments and their weighted/correlation extensions are prior art. The harmonic-strip Fejer combination and the resulting full-strip-versus-frontier resolution tradeoff are exact deductions from those classical moments; no novelty claim is made. The negative scope is limited to the canonical first-moment Landau--Gonek/positive-harmonic-kernel route as a way to exclude the sparse unattained phase-pinned frontier left by `PL-161`--`PL-162`.

## The prime-power moments already contain the desired horizontal/phase coupling

Let

`S_k(T)=sum_(zeta(rho)=0, 0<Im rho<=T) p^(k rho)`,

with zeros counted with multiplicity and with `T` chosen away from a zero ordinate when convenient. Gonek's uniform form of Landau's formula gives, for integer `x>1`,

`sum_(0<Im rho<=T) x^rho`
` = -(T/(2 pi)) Lambda(x)`
`   + O(x log(2xT) log log(3x))`.

At `x=p^k`, `Lambda(p^k)=log p`, so every prime-power depth along one exponent-lattice axis gives an arithmetic moment of the zero divisor.

The functional equation and Schwarz symmetry make the positive-ordinate zero multiset invariant under

`rho=beta+i gamma -> 1-conj(rho)=1-beta+i gamma`.

Therefore, writing `y=(beta-1/2)log p` and `theta=gamma log p`,

`Re(p^(-k/2) S_k(T))`
` = sum e^(k y) cos(k theta)`
` = sum cosh(k y) cos(k theta)`.

The second equality is exact because reflection permutes the same multiset, so the sum with `e^(k y)` equals the sum with `e^(-k y)` and may be averaged. This also handles critical-line zeros without any artificial doubling.

This is exactly the coupling demanded after `PL-162`: large `beta` increases the radial weight while `gamma log p` is the angular Fourier variable. It does not require continuing an Euler product into the strip. It comes from the completed zero set through the classical Landau explicit-formula machinery.

## Full-critical-strip Fejer positivity is exact

Let

`F_K(theta)=1+2 sum_(1<=k<K)(1-k/K) cos(k theta)`.

This is the standard Fejer kernel and is nonnegative. Set `A=(log p)/2` and let `H_(p,K)` be its symmetric harmonic extension from the two boundary components `y=+/-A` of the periodic strip:

`H_(p,K)(y,theta)`
` = 1+2 sum_(1<=k<K)(1-k/K)`
`        cosh(k y)/cosh(k A) cos(k theta)`.

Each Fourier mode `cosh(k y) cos(k theta)` is harmonic for `partial_y^2+partial_theta^2`. On either boundary `y=+/-A`, the quotient of hyperbolic cosines is `1`, so

`H_(p,K)(+/-A,theta)=F_K(theta)>=0`.

The minimum principle on the compact periodic strip then gives

`H_(p,K)(y,theta)>=0` for `|y|<=A`.

All nontrivial zeta zeros lie in the open critical strip, so each summand in `Z_(p,K)(T)` is nonnegative. This is genuine positivity before any hypothesis on RH.

Using the exact moment identity above,

`Z_(p,K)(T)`
` = N(T)
`   +2 sum_(1<=k<K)(1-k/K)/cosh(kA)`
`       Re(p^(-k/2)S_k(T)).`

Since

`p^(-k/2)/cosh(kA)=2/(p^k+1)`,

this becomes

`Z_(p,K)(T)`
` = N(T)+4 sum_(1<=k<K)(1-k/K) Re S_k(T)/(p^k+1)`.

The prime-power main term is therefore completely explicit and of order `T`; the leading population remains `N(T)~(T/(2 pi))log T`, exactly as in the unweighted finite-torus discrepancy of `PL-162`.

For the error, the factor `p^k/(p^k+1)` is bounded. Summing Gonek's integer error over `k<K` gives the displayed `O_p(K(log T+K) loglog(...))` type bound. The precise logarithmic packaging is secondary here; the important cancellation is the absence of an exponential `p^(cK)` loss at the **full** strip width.

## Positivity at the trivial strip edge prevents arbitrary interior phase resolution

Suppose RH fails and let

`Theta=sup {Re rho : zeta(rho)=0}`,

as in `PL-160`--`PL-162`. If `Theta<1`, put

`B=(Theta-1/2)log p`,  `0<B<A`.

Every zero then satisfies `|y_rho|<=B`. For `|y|<=B`,

`cosh(k y)/cosh(k A) <= 2 exp(-k(A-B))`
` = 2 p^(-k(1-Theta)).`

It follows uniformly in `K` that

`0<=H_(p,K)(y,theta)`
` <= 1+4 sum_(k>=1) p^(-k(1-Theta))`
` = 1 + 4/(p^(1-Theta)-1)`

throughout the hypothetical zero strip.

Thus letting `K` grow does **not** make the positive full-strip kernel into an increasingly sharp detector of a phase-pinned zero at `beta=Theta`. Its angular resolution saturates at a scale determined by the harmonic distance from the zero frontier to the trivial boundary `beta=1`. A sequence of isolated or arbitrarily sparse zeros with `beta_j->Theta` and `p^(i gamma_j)->1`, as left possible by `PL-161`, contributes only a uniformly bounded amount per zero to this family.

This is not a defect of the Fejer coefficients specifically. It is the ordinary smoothing of harmonic extension from a boundary separated by positive strip distance. The Fejer choice is useful because it makes both positivity and the exact prime-power Fourier calculation transparent.

If `Theta=1`, this interior damping disappears because the hypothetical frontier itself reaches the trivial strip edge. The present argument then supplies no narrower positive strip and makes no claim to exclude that possibility.

## Narrowing positivity to the hypothetical frontier destroys the uniform explicit-formula control

One can try to recover phase resolution by moving the positivity boundary inward. For `0<B<A`, define

`H_(B,K)(y,theta)`
` = 1+2 sum_(1<=k<K)(1-k/K)`
`        cosh(k y)/cosh(k B) cos(k theta)`.

The same minimum-principle argument gives `H_(B,K)>=0` on `|y|<=B`, and now

`H_(B,K)(B,0)=F_K(0)=K`.

So if `B` is chosen from a hypothetical frontier `Theta`, this kernel has exactly the desirable behavior: a zero simultaneously near `beta=Theta` and prime phase identity can acquire response of order `K`.

But the zero moment formula now reads

`sum H_(B,K)(y_rho,theta_rho)`
` = N(T)+2 sum_(1<=k<K)(1-k/K)`
`       [p^(-k/2)/cosh(kB)] Re S_k(T)`.

Multiplying Gonek's `O(p^k log(2p^kT)loglog(3p^k))` error by the `k`th coefficient produces

`O( [p^(k/2)/cosh(kB)] log(2p^kT)loglog(3p^k) ).`

For

`B=(Theta-1/2)log p`,

and fixed `Theta>1/2`,

`p^(k/2)/cosh(kB) asymp p^(k(1-Theta)).`

The error bound therefore grows exponentially in the Fourier degree whenever `Theta<1`, while the target boundary response of one phase-pinned zero grows only linearly as `K`. The theorem that gives the arithmetic prime-power main term is consequently too coarse to certify the absence of an arbitrarily sparse near-frontier sequence by this positive localization.

This statement is deliberately about the **available uniform Landau--Gonek bound**, not a theorem that the true remainder must be that large. A substantially sharper explicit formula, with an error exponent lying below the targeted frontier, could change the conclusion. The point is that the classical uniform formula does not supply such a gain.

## Existing weighted Landau--Gonek extensions are statistical, not sparse-frontier exclusion theorems

Farzad Aryan's peer-reviewed extension makes this boundary especially relevant. Aryan inserts Gaussian and Fejer-type local zero-correlation weights into the Landau--Gonek framework and obtains unconditional pair-correlation information. In his Theorem 1.1, an off-critical zero produces a large positive local contribution, but cancellation can come from zeros sufficiently close to it. The resulting Corollary 1.2 gives a strong sparsity bound only after a non-clustering hypothesis; the paper explicitly identifies clustering as the troublesome missing control.

This is close prior art to the desired `PL-162` repair. It shows that adding horizontal sensitivity and local zero statistics to Landau--Gonek is already an established program, and that the output is naturally a density/correlation statement. It does not prove that **no** sparse sequence of zeros can approach an unattained rightmost frontier while simultaneously satisfying `p^(i gamma_j)->1`.

The 2026 preprint of Durkan--Hughes--Pearce-Crump further generalizes Landau--Gonek by studying sums of `chi(rho)X^rho`, with different asymptotic regimes according to `X/T`. It confirms that functional-equation-weighted zero moments remain an active and powerful mean-value tool, but it does not supply the missing exclusion of an arbitrarily sparse off-critical frontier. It is used here only as current prior-art context, not as theorem-level support for the derived obstruction.

## Relation to PL-161 and PL-162

`PL-161` leaves, under one-sided fixed-step boundedness and RH failure, a coupled necessary condition

`beta_j -> Theta`,  `exp(i gamma_j log p) -> 1`.

`PL-162` shows that the second condition alone is vertically generic over the full zero population, even simultaneously for every fixed finite family of prime axes. It therefore proposes conditioned or weighted prime-phase information that retains `beta` as the next meaningful target.

The present finding performs the cheapest such weighted test. The canonical moments

`p^(k rho)=p^(k beta) exp(i k gamma log p)`

already retain both coordinates and are governed by Landau--Gonek. Positive Fejer assembly then exposes a structural tradeoff:

- use the full critical-strip boundary and the explicit-formula errors remain controlled, but harmonic damping prevents increasing resolution of a frontier strictly inside `beta=1`;
- move the positive boundary to the hypothetical frontier and the desired `K`-scale phase localization returns, but the known uniform arithmetic error grows as `p^(K(1-Theta))`.

So `PL-162` should not be followed merely by "insert `p^(k beta)` weights and a positive trigonometric kernel." That route is both classicalized and quantitatively unable, with current uniform estimates, to eliminate the sparse unattained frontier left by `PL-160`--`PL-161`.

## Prior art and novelty audit

Primary anchors:

- **S. M. Gonek**, “A Formula of Landau and Mean Values of `zeta(s)`,” in *Topics in Analytic Number Theory*, ed. S. W. Graham and J. D. Vaaler, University of Texas Press, 1985, pp. 92--97. Gonek gives the uniform Landau formula used here. Farzad Aryan quotes the integer specialization in equation (1.1), exactly in the form needed for the prime-power calculation.
- **S. M. Gonek**, “An explicit formula of Landau and its applications to the theory of the zeta-function,” in *A Tribute to Emil Grosswald: Number Theory and Related Analysis*, Contemporary Mathematics **143**, AMS, 1993, pp. 395--413. Classical extended reference for the uniform explicit formula.
- **Farzad Aryan**, “On an extension of the Landau-Gonek formula,” *Journal of Number Theory* **233** (2022), 389--404. DOI `10.1016/j.jnt.2021.06.015`; arXiv `1902.05473`. Theorem 1.1 and Section 1.1 introduce local Gaussian/Fejer zero-correlation weights, and Corollary 1.2 illustrates the resulting off-line zero-density information under non-clustering.
- **Benjamin Durkan, Christopher Hughes, Andrew Pearce-Crump**, “Generalisations of the Landau--Gonek Theorem and applications to mean values of zeta,” arXiv `2601.18025` (submitted 25 January 2026). Current extension with a `chi(rho)X^rho` weight; used only for modern prior-art context.

A targeted search around Landau--Gonek with Fejer/Poisson/harmonic-strip kernels, horizontal zero weights, and off-critical localization located Aryan's correlation-weight extension and standard pair-correlation descendants, but not an exact published statement of the symmetric strip-harmonic Fejer identity above. That absence is not evidence of novelty. The identity is elementary once Gonek's moments and the functional-equation reflection symmetry are combined, and it is classified only as exact derived structure.

## Adversarial boundaries

1. **This does not rule out all weighted prime-phase methods.** It rules out a specific natural route: finite Landau--Gonek moments assembled through positive harmonic Fejer localization, with control supplied by the standard uniform Gonek remainder.

2. **The Gonek error is an upper bound, not a lower bound.** Exponential loss after narrowing the strip proves that the available theorem cannot certify sparse-frontier exclusion at increasing phase resolution. It does not prove that a sharper cancellation estimate is impossible.

3. **Aryan's extensions can detect statistical off-line mass.** The negative conclusion is about an arbitrarily sparse unattained frontier. A theorem forcing such a frontier to have positive density or a controlled local cluster geometry could make existing weighted correlation formulas decisive.

4. **The full-strip kernel is positive for analytic reasons, not because RH is true.** Its positivity is inherited from boundary Fejer positivity by the minimum principle and therefore cannot itself localize zeros to `beta=1/2`.

5. **The factor `1/2` is not selected anew.** It enters the moment symmetrization through the functional equation `beta <-> 1-beta`. The new calculation does not claim an independent geometric derivation of the critical line.

6. **The prime axis is arithmetically real but not sufficient.** Choosing `x=p^k` is what produces the von-Mangoldt main term, so this is not generic Kronecker geometry. Nevertheless the prime-power arithmetic main term controls a population statistic rather than forbidding a sparse phase-pinned edge.

7. **No Euler product is analytically continued.** The argument uses the zero-side Landau--Gonek explicit formula and the functional-equation symmetry of the completed zeta divisor. The only Euler-side arithmetic input is the classical von-Mangoldt main term at the integer prime powers.

8. **The case `Theta=1` remains outside the narrowed-strip obstruction.** If a hypothetical zero frontier has supremum `1`, the harmonic distance to the trivial strip boundary vanishes and the `p^(K(1-Theta))` tradeoff degenerates. No exclusion of that case is claimed.

A falsification of the exact derived part would require failure of the functional-equation reflection identity for the positive-ordinate zero multiset, failure of the harmonic minimum-principle positivity, an algebraic error in the factor `4/(p^k+1)`, or failure of the standard integer Landau--Gonek estimate at `p^k`.

## Consequence for the research line

The live problem after `PL-162` is narrower than a generic "horizontal-weighted phase theorem." The classical Landau--Gonek family already provides those weights, and standard positive localization faces the full-strip/frontier resolution tradeoff above.

To close the `PL-161` lower-bounded fixed-ray loophole, a useful new input would need at least one feature absent here: a theorem forcing substantial density or non-clustering structure on zeros approaching a hypothetical `Theta`; a positive/local identity in which a **single** near-frontier off-line zero has an uncancellable contribution; a genuinely sharper uniform explicit formula whose remainder beats the `X^Theta` target at the required resolution; or a different arithmetic coupling not reducible to first-moment prime-power Landau--Gonek data.

That sparse-frontier sensitivity, rather than ordinary finite-prime phase distribution or classical weighted zero moments, is now the relevant target.