# Farey-discrepancy research lines

This file records the current mathematical questions that survive the Farey-discrepancy evidence. It is not a roadmap, task queue, status page, or history.

## Force block-Mertens magnitude past the positive-capacity boundary; sign polarization is no longer the near-capacity gate under RH

FD-255--FD-265 separate the signed exact-omission threshold from the physical nonnegative-source boundary. The positive switched-response cone has a genuine capacity loss, while canonical full-grid inversion supplies only `O(D log D)` repair mass after explicit forcing terms are removed. Dense deep blocks or a negative signed mean therefore do not by themselves produce the one-sided amplification required by the physical destination.

FD-298 reduces the low-height zero-safe hard-complement problem, below the aggregate rigidity floor, to the original block-Mertens field

`G_N(d)=sum_(q|d) [M(Nq)-M(N(q-1))]`

at the physical band scale. With `L_N(x)=sum_(x<d<=2x)|G_N(d)|`, the near-capacity budget is `B_(N,x)=N^(1/2)x^(1+c)/ell(x)`, where `c=1-log_2(3/2)` and `ell` is subpolynomial.

FD-299 resolves the sign-polarization loophole at that scale under RH. The signed band sum `S_N(x)=sum G_N(d)` is an exact probability average of `M(Nq)` under the divisor-replication law, whose moments `E(q^alpha)` are uniformly bounded for every `alpha<1`. RH therefore gives `|S_N(x)|<=N^(1/2)x^(1+o(1))=o(B_(N,x))`. Whenever `L_N(x)` itself is a fixed fraction of `B_(N,x)`, the positive and negative masses are consequently each `L_N(x)/2+o(B_(N,x))`; for the canonical real repair the one-sided negative demand is `L_N(x)/4+o(B_(N,x))`. The same sign balance transfers to every zero-safe hard complement inside the FD-298 rigidity regime because its `l^1` distance from `G_N` is `o(B_(N,x))`.

The live deterministic source question is therefore the **post-convolution magnitude** `L_N(x)`, not an independent sign-bias theorem. Prove a lower bound for `L_N(x)` at the near-capacity scale in the physical polynomial-depth regime, or prove that the block-Mertens convolution cannot reach that scale. The argument must retain the exact divisor-replication geometry: neither a large raw Mertens fluctuation nor an unsigned pre-convolution estimate automatically yields the required `l^1` field. The sign-balance reduction is conditional on the Mertens growth input used in FD-299, in particular RH for the stated half-power bound.

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

The low-height gate is therefore static rather than a return-frequency problem. Below the FD-296/FD-297 rigidity threshold, the decisive source question is to estimate one fixed baseline `R_(T_bullet,N)` at the physical band scale. FD-298--FD-299 sharpen that baseline question in the regime where the hard complement is `l^1`-close to the block-Mertens field: under RH, one-sided sign polarization cannot decide the near-capacity classification, so the remaining scalar source quantity is the magnitude `L_N(x)`. If the baseline lies inside the near-capacity target by a fixed margin, every zero-safe cutoff throughout the controlled range is good; if it lies outside by a fixed margin, moving the hard cutoff cannot repair it.

Above that threshold but still inside the FD-295 short-complete-packet regime, one must still prove near-linear safe occupation directly or obtain a stronger path-control theorem. If the fixed low-height baseline cannot be controlled from the physical source, the unresolved mathematics is no longer “find a first return” but derive a direct estimate for that exact complete hard complement or replace the phase/remainder coupling mechanism.

The current Montgomery--Vaughan selector still cannot be rerun gap by gap. The FD-292 estimate on an interval of length `R` requires `R/L^(2m(m+2))->infinity` for fixed moment order `m`, whereas every individual RH zero gap has `R<<1/log log H`. The phase theorem is therefore intrinsically aggregate at zero-gap scale. This is a limitation of that implementation, not a theorem that finer local phase control is impossible.

This sharpening remains conditional where stated. FD-297 turns the low-height search into a fixed-baseline dichotomy only under its global background control and zero-safe complete-cluster geometry; FD-298--FD-299 identify a more explicit low-height source field and remove sign polarization under the stated Mertens/RH input, but they do not prove the required lower bound for `L_N(x)`. FD-294 still requires the occupation and complete-packet hypotheses it consumes outside the rigidity regime, and FD-295 only removes capacity for short complete packets in its stated range. Any attempt to replace the physical grouped remainder by a generic Möbius/Mellin estimate must re-prove that it controls the exact gapwise destination quantity; if it loses the Farey divisor-replication geometry, the natural ownership moves to `mobius_cancellation`.
