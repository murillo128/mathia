# Farey-discrepancy research lines

This file records the current mathematical questions that survive the Farey-discrepancy evidence. It is not a roadmap, task queue, status page, or history.

## Force block-Mertens magnitude past the positive-capacity boundary; in the deepest RH regime the carrier compresses to an additive spectral spike

FD-255--FD-265 separate the signed exact-omission threshold from the physical nonnegative-source boundary. The positive switched-response cone has a genuine capacity loss, while canonical full-grid inversion supplies only `O(D log D)` repair mass after explicit forcing terms are removed. Dense deep blocks or a negative signed mean therefore do not by themselves produce the one-sided amplification required by the physical destination.

FD-298 reduces the low-height zero-safe hard-complement problem, below the aggregate rigidity floor, to the original block-Mertens field

`G_N(d)=sum_(q|d) [M(Nq)-M(N(q-1))]`

at the physical band scale. With `L_N(x)=sum_(x<d<=2x)|G_N(d)|`, the near-capacity budget is `B_(N,x)=N^(1/2)x^(1+c)/ell(x)`, where `c=1-log_2(3/2)` and `ell` is subpolynomial.

FD-299 resolves the sign-polarization loophole at that scale under RH. The signed band sum `S_N(x)=sum G_N(d)` is an exact probability average of `M(Nq)` under the divisor-replication law, whose moments `E(q^alpha)` are uniformly bounded for every `alpha<1`. RH therefore gives `|S_N(x)|<=N^(1/2)x^(1+o(1))=o(B_(N,x))`. Whenever `L_N(x)` itself is a fixed fraction of `B_(N,x)`, the positive and negative masses are consequently each `L_N(x)/2+o(B_(N,x))`; for the canonical real repair the one-sided negative demand is `L_N(x)/4+o(B_(N,x))`. The same sign balance transfers to every zero-safe hard complement inside the FD-298 rigidity regime because its `l^1` distance from `G_N` is `o(B_(N,x))`.

FD-300 turns any near-capacity lower bound for `L_N(x)` into a sharper necessary source-energy statement. Writing `U_N(q)=M(Nq)-M(N(q-1))`, if `L_N(x)>=B_(N,x)x^{-o(1)}`, then some dyadic divisor shell `Q<q<=2Q` must satisfy

`(1/Q) sum_(Q<q<=2Q) |U_N(q)|^2 >= N x^(2c-o(1))`.

Equivalently the shell RMS must reach `N^(1/2)x^(c-o(1))`. A uniform fixed-power saving below that threshold rules out the near-capacity route. FD-301 demasks the resulting aligned same-block correlation at logarithmic Fourier cost, forcing a rational additive-twist two-point Möbius sum, and FD-302 shows that the genuinely twisted alternative can be confined to a low block-Fourier arc.

FD-303 shows that sufficiently large aligned shell variance cannot remain a pathology of the aligned starts or their periodic mask. Let `S_N(y)=M(y+N)-M(y)` and `X=NQ`. The elementary `2`-Lipschitz dependence of `S_N(y)` on the start thickens every large aligned increment into a disjoint interval of nearby starts, giving

`J_mu(X,N)=sum_(X<=y<2X)|S_N(y)|^2 >> Q E_Q^(3/2)`

when the shell energy `E_Q=(1/Q)sum|U_N(q)|^2` tends to infinity in the stated polynomial-depth regime. Under a fixed near-capacity lower bound and `x=N^(lambda+o(1))`, this forces

`J_mu(X,N)/(XN) >= N^(3c lambda-1/2-o(1))`.

Hence once `lambda>1/(6c)=0.401570...`, the complete sliding second moment is polynomially superdiagonal. Expanding that moment forces a polynomially thick family of ordinary untwisted positive Möbius correlations, occupying polynomially many pairs and therefore many distinct shifts.

FD-304 adds two RH-conditional rigidities to this deep regime. First, every capacity-bearing shell must lie at denominator depth

`Q >= x^(2c-o(1))`,

and for every fixed `eta>0` it contains at least `x^(2c-o(1))` blocks with `|U_N(q)|>=N^(1/2)x^(c-eta)`, hence power-many large Mertens grid endpoints. Near-capacity mass therefore cannot be carried by one exceptional aligned block. Second, for the canonical fixed-window correlations

`C_h^0(X)=sum_(X<=n<2X) mu(n)mu(n+h)`, `X=NQ`,

the moving-start correlations from FD-303 differ by at most `2N`. The shell-depth floor makes this boundary cost negligible by a fixed power once

`lambda>3/(10c)=0.7228262519...`.

In that range near-capacity mass forces at least `N^(-1/2)x^(3c-o(1))` distinct shifts `1<=h<N` on the same interval `[X,2X)` with

`C_h^0(X) >= Q N^(-1/2)x^(3c-o(1))`.

FD-305 compresses that entire common-window family into one exact additive-spectral certificate. For `f_X(n)=mu(n)1_[X,2X)(n)` and `F_X(alpha)=sum f_X(n)e(n alpha)`, trimming the common-window correlations to compact autocorrelations costs at most `N`, which is already negligible in the FD-304 range. Wiener--Parseval then gives

`int_0^1 |F_X(alpha)|^4 d alpha = sum_h |R_h(X)|^2`

and therefore

`int_0^1 |F_X(alpha)|^4 d alpha >= Q^2 N^(-3/2) x^(9c-o(1))`.

Relative to the natural `X^2` scale this is `N^(-7/2)x^(9c-o(1))`. Once

`lambda>7/(18c)=0.9369969932...`,

the fourth moment is forced power-above `X^2`, and the second-moment bound also forces at least one source-selected frequency `alpha_*` with

`|F_X(alpha_*)|/X^(1/2) >= N^(-7/4)x^(9c/2-o(1))`.

This is a one-way deterministic compression of the FD-304 family; it neither localizes `alpha_*` nor contradicts classical logarithmic Möbius exponential-sum bounds.

The live deterministic source question is therefore regime-dependent and sharper than the original masked correlation problem. For `lambda>7/(18c)`, exclude the **fixed-block additive spectral concentration forced by FD-305**, either through the fourth moment or a sufficiently strong uniform pointwise bound at the source-selected scale `X=NQ`. For `3/(10c)<lambda<=7/(18c)`, the FD-305 lower bound still holds but need not be power-above the natural fourth-moment scale, so the FD-304 common-window Chowla-type family remains the stronger quantitative carrier. For `1/(6c)<lambda<=3/(10c)`, the FD-303 moving-start family is the strongest established carrier. Below that threshold, or where FD-303 amplification is not superdiagonal, the FD-301--FD-302 untwisted/low-block-frequency family remains the finer necessary carrier. These implications are one-way: deep shells, large Mertens endpoints, large ordinary correlations or a large additive Fourier coefficient do not by themselves reconstruct a near-capacity `L_N(x)` field.

## Force physical occupation of the complete zero-packet regime

FD-282--FD-287 show that the grouped strict-right Perron collar retains a prime witness unless an order-`L` near-one `zeta'/zeta` phase event occurs. FD-288--FD-289 make those events sparse uniformly in translated polynomial windows, and FD-290 shows phase-good and zero-safe cluster-complete heights coexist. FD-291 then uses the exact constancy of the complete hard complementary remainder on each zero gap: a remainder-good gap can be trimmed internally by reciprocal-log collars and stays remainder-good throughout its safe core.

FD-292 removes any distinguished inverse-polylog exponent from the phase side. Applying the same Montgomery--Vaughan mean-square theorem to fixed powers of the strict-right logarithmic derivative gives, for every prescribed fixed `P>0`, phase-bad measure `O_P(H/L^P)` on polynomial windows. It is therefore enough, in principle, to prove reciprocal-log-safe occupation `Omega_B(J)>=delta_P H/L^P` for the **complete physical hard remainder** at one convenient fixed `P`.

FD-293 shows that this apparently weak measure target has a strong population cost under RH. The classical RH zero-gap cap

`gamma_(j+1)-gamma_j <= (pi+o(1))/log log H`

implies that any such occupation certificate forces at least

`K_B(J) >= (delta_P/pi-o(1)) H log log H/L^P = H^(1-o(1))`

remainder-good gaps in the relevant polynomial window. Finitely many good gaps, a sparse exceptional sequence, or `O(H^alpha)` good gaps for fixed `alpha<1` cannot close the FD-292 route. The count is only necessary, not sufficient: the safe cores must still contribute enough total length.

FD-294 converts that missing occupation statement into the cancellation resource the route actually needs. Under its stated zero-gap population, safe-occupation and complete-packet hypotheses, near-linear occupation by good gaps forces near-linear many **short complete zero-packet cancellations**. The phase synchronization therefore does not have to be rebuilt independently on every occupied gap once the packet lies in the complete regime; the load-bearing missing input is physical occupation of enough such packets.

FD-295 removes a second possible bottleneck below square-root height. Short complete zero packets in that range are automatically capacity-subcritical. Thus, once completeness and the required source occupation are established there, a separate packet-capacity estimate is not an additional gate. This is a regime statement: it does not make incomplete packets harmless and it does not extend the conclusion beyond the square-root-height range proved in FD-295.

FD-296 identifies a lower-height regime in which the occupation gate collapses to path rigidity. Under RH, simple zeros and the stated desingularized-background bound, the exact FD-280 telescoping identity and the FD-278 aggregate cluster ledger give a capacity-subcritical diameter for the zero-safe hard-remainder path across one dyadic height window whenever

`Delta(tau,lambda,b)=c-b-tau-kappa(tau,lambda)>0`,

with `c=1-log_2(3/2)` and `kappa(tau,lambda)=tau/[2(1-tau/(pi(1+1/lambda)))]`. In that regime the path diameter is `o(C_(N,x)/ell(x))` for every subpolynomial `ell`, so one buffered good point propagates through the safe part of the window.

FD-297 removes even that dyadic first-return requirement. Fix any low height `T_bullet` inside a nontrivial-zero gap and strengthen the background hypothesis to a single desingularized envelope over every complete reciprocal-log component below `H=x^(tau+o(1))`. Under the same inequality `Delta(tau,lambda,b)>0`, the exact-complement identity gives

`sup_(T zero-safe, T_bullet<=T<=H) ||R_(T,N)-R_(T_bullet,N)||_(1,x) = o(B_(N,x))`

for every near-capacity budget `B_(N,x)=C_(N,x)/ell(x)` with subpolynomial `ell`. Consequently the whole low-height zero-safe trajectory has the same good/bad classification, up to an `o(B)` transition layer, as one **fixed low-height complete hard remainder**. Replacing `T_bullet` by another fixed admissible gap changes the normalized baseline only by `o(1)`, so this is not a tuned-anchor effect.

The low-height gate is therefore static rather than a return-frequency problem. Below the FD-296/FD-297 rigidity threshold, the decisive source question is to estimate one fixed baseline `R_(T_bullet,N)` at the physical band scale. FD-298--FD-305 sharpen that baseline question in the regime where the hard complement is `l^1`-close to the block-Mertens field: under RH, one-sided sign polarization cannot decide the near-capacity classification; near-capacity mass forces aligned shell energy; RH pushes every carrying shell past `x^(2c-o(1))` and makes it power-populated; the correlation carrier first demasks to an untwisted/low-frequency family, then thickens into moving-start ordinary correlations, then moves onto one canonical interval, and at the deepest polynomial scales compresses further into an additive Fourier fourth-moment/pointwise spike. A cancellation theorem at whichever exact source carrier is strongest in the relevant regime would close the low-height near-capacity route before one has to prove a matching `l^1` lower bound.

Above that threshold but still inside the FD-295 short-complete-packet regime, one must still prove near-linear safe occupation directly or obtain a stronger path-control theorem. If the fixed low-height baseline cannot be controlled from the physical source, the unresolved mathematics is no longer “find a first return” but derive a direct estimate for that exact complete hard complement or replace the phase/remainder coupling mechanism.

The current Montgomery--Vaughan selector still cannot be rerun gap by gap. The FD-292 estimate on an interval of length `R` requires `R/L^(2m(m+2))->infinity` for fixed moment order `m`, whereas every individual RH zero gap has `R<<1/log log H`. The phase theorem is therefore intrinsically aggregate at zero-gap scale. This is a limitation of that implementation, not a theorem that finer local phase control is impossible.

This sharpening remains conditional where stated. FD-297 turns the low-height search into a fixed-baseline dichotomy only under its global background control and zero-safe complete-cluster geometry; FD-298--FD-305 identify a more explicit low-height source field, remove sign polarization under the stated Mertens/RH input, expose a necessary aligned variance tariff, localize any capacity-bearing shell under RH, and progressively demask its correlation consequence to a common-window ordinary family and then an additive-spectral certificate in the deepest regime. They do not prove the required lower bound for `L_N(x)` or show that any of those necessary anomalies are sufficient. FD-294 still requires the occupation and complete-packet hypotheses it consumes outside the rigidity regime, and FD-295 only removes capacity for short complete packets in its stated range. Any attempt to replace the physical grouped remainder by a generic Möbius/Mellin estimate must re-prove that it controls the exact gapwise destination quantity; once the Farey divisor-replication geometry has been discharged and only the fixed-window Möbius or additive-spectral carrier remains, the natural ownership moves to `mobius_cancellation`.
