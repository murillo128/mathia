# VIS-058 — overlapping-triple dependence yields a process-aware Fisher-orientation error certificate

## Claim

Let `(G_t)_(t in Z)` be a stationary process on a finite alphabet, and let

`Y_t = (G_t,G_(t+1),G_(t+2))`

be its overlapping three-symbol process. Write `C` for the declared finite triple support, `K=|C|`, and let `P` be the stationary law of `Y_t`. From `n` consecutive overlapping triples define the empirical law

`P_hat_n(c) = (1/n) sum_(t=1)^n 1{Y_t=c}`.

Put

`q = sum_(c in C) P(c)^2`,
`c_h = Pr(Y_0=Y_h)`.

Then the mean squared `L^2` error of the empirical triple law has the exact finite-sample identity

`V_n := E ||P_hat_n-P||_2^2`
` = (1/n^2) [ n(1-q) + 2 sum_(h=1)^(n-1) (n-h)(c_h-q) ].`

Thus the full empirical-law second moment depends on the process only through the lagged **triple-collision excesses** `c_h-q`. In particular, if nonnegative numbers `b_h` satisfy

`|c_h-q| <= b_h`,

then

`V_n <= Vbar_n`
` := (1/n^2) [ n(1-q) + 2 sum_(h=1)^(n-1) (n-h)b_h ].`

No independence of the overlapping triples is required.

A standard mixing envelope is one sufficient way to provide the long-lag `b_h`. Define, for the underlying symbol process, the absolute-regularity coefficient in the explicit total-variation convention

`beta(r)`
` = sup_t || Law(G_(-infinity:t),G_(t+r:infinity))`
`            - Law(G_(-infinity:t)) tensor Law(G_(t+r:infinity)) ||_TV.`

For `h>=3`, the first triple ends at time `2` and the second starts at time `h`, so

`|c_h-q| <= beta(h-2)`.

The overlap lags `h=1,2` remain separate finite-range terms; they may be computed or bounded directly rather than pretending that the triples are independent.

Since `||x||_1^2 <= K ||x||_2^2`, every valid upper bound `Vbar_n` gives the high-probability raw-law radius

`Pr( ||P_hat_n-P||_1 > delta_rho ) <= rho`,
`delta_rho = sqrt(K Vbar_n / rho)`,

for every `0<rho<1`. This is deliberately a coarse second-moment certificate, not a sharp concentration theorem.

Now freeze one strictly positive common Fisher reference law `H` on the same support as in `VIS-041`, with

`h_min = min_c H(c) > 0`.

Let `Delta(P)=P-M(P)` be the adjacent-pair Markov residual from `VIS-057`, and write

`e_hat = ||Delta(P_hat_n)||_H`.

On the event `||P_hat_n-P||_1 <= delta_rho`, define

`a_rho = 6 delta_rho / sqrt(h_min)`.

Then `VIS-057` gives

`||Delta(P_hat_n)-Delta(P)||_H <= a_rho`

and hence

`||Delta(P)||_H >= e_hat-a_rho`.

If the **observable margin gate**

`e_hat > 2 a_rho`

holds, the population residual is nonzero and its normalized Fisher direction differs from the empirical normalized direction by at most

`2 a_rho / (e_hat-a_rho)`.

For two stationary processes `A,B`, with separately justified radii and the same frozen `H`, the union bound therefore gives probability at least `1-rho_A-rho_B` that

`|kappa_H(P_hat^A,P_hat^B)-kappa_H(P^A,P^B)|`
` <= min(2,`
`      2 a_A/(e_hat_A-a_A)`
`    + 2 a_B/(e_hat_B-a_B))`

whenever `e_hat_r>2a_r` for both processes.

So a process-aware dependence bound can now be propagated through **overlapping triple estimation -> recomputed nonlinear Markov closure -> Fisher residual normalization -> signed cross-process orientation** without inserting an i.i.d. multinomial approximation.

**Evidence/status:** `EXACT-DERIVED + STANDARD DEPENDENT-EMPIRICAL-MEASURE ASSEMBLY + PROCESS-AWARE SAMPLING INTERFACE + NO-NOVELTY-CLAIM`.

No mixing law is asserted for Riemann zeros or finite CUE, no finite zeta window is turned into a random sample by this theorem, no sharpness is claimed for the Markov/second-moment constants, and no RH consequence follows from satisfying the displayed margin gate.

## 1. The exact second moment remembers overlap only through collision covariance

For one cell `c`, let

`I_t(c)=1{Y_t=c}`.

Stationarity gives `E I_t(c)=P(c)`. Expanding the empirical error and summing over cells,

`E ||P_hat_n-P||_2^2`
` = (1/n^2) sum_c sum_(s,t=1)^n Cov(I_s(c),I_t(c)).`

For `s=t`,

`sum_c Var(I_t(c))`
` = sum_c P(c)(1-P(c))`
` = 1-q`.

For a positive lag `h`,

`sum_c Cov(I_0(c),I_h(c))`
` = sum_c [Pr(Y_0=c,Y_h=c)-P(c)^2]`
` = Pr(Y_0=Y_h)-q`
` = c_h-q`.

There are `n-h` ordered pairs at lag `h` in each direction. This proves the exact identity for `V_n`.

The formula is useful precisely because adjacent overlapping triples are not independent observations. Their short-lag dependence is represented explicitly by `c_1-q` and `c_2-q`; all longer dependence is carried by the remaining collision sequence. Negative lag covariance is allowed and can reduce the exact variance. The upper envelope uses absolute values only when a one-sided certificate is needed.

As a sanity check, if the underlying symbols are i.i.d. and the induced triple law is uniform, the overlap itself need not inflate this aggregate `L^2` second moment: for the uniform law the diagonal collision probability at the first two lags equals `q`. This is another reason not to replace "overlapping" by an automatic effective-sample-size penalty without inspecting the actual dependence structure.

## 2. Absolute regularity is one sufficient long-lag envelope

For `h>=3`, `Y_0` is measurable with respect to the past block ending at time `2`, while `Y_h` is measurable with respect to the future block beginning at time `h`. Under the displayed total-variation definition of `beta`, the joint law of `(Y_0,Y_h)` differs from `P tensor P` by at most `beta(h-2)` in total variation.

Apply that bound to the diagonal event

`D={(y,y): y in C}`.

Under the joint law its probability is `c_h`; under `P tensor P` it is `q`. Hence

`|c_h-q| <= beta(h-2)`.

This step uses only the defining total-variation domination of events. Stronger covariance or empirical-process results from the mixing literature may provide sharper rates, but none is needed for the finite identity or for this sufficient envelope.

For example, keeping direct short-lag bounds `b_1,b_2` and a long-lag beta envelope gives

`Vbar_n`
` = (1/n^2) [ n(1-q)`
`   + 2(n-1)b_1 + 2(n-2)b_2`
`   + 2 sum_(r=1)^(n-3) (n-r-2) beta(r) ].`

If `sum_r beta(r)<infinity`, this certificate has the expected `O(1/n)` second-moment scale for fixed finite support, but the exact constant still depends on the actual overlap and dependence structure. Summability is a sufficient asymptotic condition here, not a claim about either zeta or CUE.

If `q` is unavailable under the chosen uncertainty model, replace `n(1-q)` by `n`. If no sharper short-lag information is available, `b_1=b_2=1` gives a completely external but correspondingly coarse certificate. The theorem therefore does not require estimating unknown population quantities from the same data and silently treating them as fixed.

## 3. Finite support converts the second moment into a raw-law confidence radius

For every vector on `K` cells,

`||x||_1 <= sqrt(K) ||x||_2`.

Therefore

`E ||P_hat_n-P||_1^2`
` <= K E ||P_hat_n-P||_2^2`
` <= K Vbar_n`.

Markov's inequality applied to the nonnegative squared `L^1` error gives

`Pr( ||P_hat_n-P||_1^2 >= K Vbar_n/rho ) <= rho`.

This proves the displayed `delta_rho`.

The price for making no distributional approximation is visible: the radius scales as `rho^(-1/2)` rather than carrying an exponential tail. That is acceptable for the present purpose because the role of the result is to expose the **missing dependence input** cleanly. If a valid sharper concentration inequality is available for the actual process, its `L^1` radius may replace `delta_rho` directly in `VIS-057` without changing any downstream Fisher geometry.

Likewise, `K` should be the predeclared common support, not a support selected after inspecting the two processes. A sparse adaptive support can make the numerical radius look better while changing the representation itself.

## 4. The residual-energy gate can be checked from the empirical law

`VIS-057` bounds the Markov-residual perturbation in the fixed common Fisher metric:

`||Delta(P_hat_n)-Delta(P)||_H`
` <= 6 ||P_hat_n-P||_1 / sqrt(h_min)`.

On the `delta_rho` event this is at most `a_rho`. The reverse triangle inequality then gives

`||Delta(P)||_H >= e_hat-a_rho`.

The usual normalized-vector inequality says that if nonzero vectors `u` and `u_tilde` satisfy `||u_tilde-u||<=a<||u||`, then

`||u_tilde/||u_tilde|| - u/||u|||| <= 2a/||u||`.

The difficulty is that the population norm `||u||` is not observed. The gate

`e_hat>2a_rho`

solves that circularity: it implies

`||Delta(P)||_H >= e_hat-a_rho > a_rho`.

Hence the normalized population residual exists and

`|| Delta(P_hat_n)/e_hat`
` - Delta(P)/||Delta(P)||_H ||_H`
` <= 2a_rho/(e_hat-a_rho)`.

For two processes, the change of the inner product of their normalized residuals is at most the sum of the two normalized-vector errors. Capping by the trivial range `[-1,1]` yields the stated orientation interval.

This is the missing observable bridge in `VIS-057`: a raw-law radius no longer has to be compared with an unknown population residual energy. A sufficiently large empirical residual supplies a conservative certificate that the normalization itself is stable.

## 5. Prior art and novelty boundary

Mixing coefficients, covariance control, empirical-process limit theory for dependent sequences, and finite-alphabet empirical measures are classical. Relevant anchors are Richard C. Bradley, **Basic properties of strong mixing conditions. A survey and some open questions**, *Probability Surveys* 2 (2005), 107–144, DOI `10.1214/154957805100000104`; P. Doukhan and J. R. León, **Invariance principles for the empirical measure of a mixing sequence and for the local time of Markov processes**, *Lecture Notes in Mathematics* 1193 (1986), 4–21, DOI `10.1007/BFb0077096`; and Emmanuel Rio, **Covariance inequalities for strongly mixing processes**, *Annales de l'I.H.P. Probabilités et Statistiques* 29:4 (1993), 587–597. These establish that dependent empirical-measure and mixing-covariance control are mature literatures, not a Mathia invention.

The exact collision identity above is an elementary finite expansion of the empirical-cell covariance, and the high-probability radius uses only finite-dimensional norm comparison plus Markov's inequality. No novelty is claimed for those ingredients, for beta mixing, or for the normalized-vector perturbation inequality.

The Mathia-specific durable content is the assembled interface to the existing visual three-gap branch: the dependence structure is reduced to a process-level second-moment/envelope input and then propagated through the already established nonlinear closure and common-Fisher orientation controls. This makes explicit what must be justified before an apparent zeta/CUE residual direction can be called statistically stable.

## 6. Boundary conditions and falsification

The triple process must have a genuine stochastic law under which stationarity and the stated dependence envelope are meaningful. A deterministic finite table of Riemann zeros does not acquire repeated-sampling semantics merely because its consecutive triples overlap. Applying the certificate to zeta requires a defensible probabilistic/process model or another uncertainty construction that supplies a valid raw-law radius.

The result is written for a two-sided stationary symbol process. A finite circular CUE eigenphase sample is not automatically an instance of that setup either. A random-root/cyclic formulation, independent-matrix sampling argument, or another finite-circle treatment must justify the corresponding radius rather than importing the stationary beta coefficients by analogy.

The partition, declared support, Markov residual construction, and common positive Fisher reference `H` are frozen. If `H` is itself estimated or changed between samples, its uncertainty is additional representation error; `VIS-045` controls deterministic gauge changes but that contribution must be composed explicitly. If a declared middle state has zero empirical or population mass, the current `VIS-057` completion hypothesis fails and the support convention must be repaired before using this certificate.

The beta envelope is only sufficient. Failure to prove beta mixing does not prove the residual direction unstable, and a different process-aware second-moment or concentration argument may be substituted. Conversely, choosing a convenient beta rate after seeing the residual is not a validation.

Falsify the exact part by finding a stationary finite-alphabet process for which the collision-covariance identity fails, an asserted beta envelope that does not dominate the long-lag diagonal event, or a case satisfying the raw-law event and `e_hat>2a_rho` in which the population normalized residual violates the displayed orientation bound.

## Research consequence

The accepted `CLUE-zeta-three-gap-cmi-equivalent-size-eight` no longer has an undefined instruction to "account for overlapping triples." The needed object is now explicit: before interpreting a higher-window zeta/CUE Fisher orientation, supply a process-appropriate upper bound on the empirical triple-law error — for example through the exact collision second moment plus a justified dependence envelope, or through a sharper valid alternative — and require the observed residual energy to clear the `e_hat>2a` gate.

This does **not** unblock the higher-window experiment by itself. The repository still lacks a justified stochastic dependence envelope or equivalent uncertainty radius for a finite zeta window, and the CUE side should continue to use its independent-matrix design rather than replacing it with this generic bound when direct replication is available.

The useful next step is therefore no longer more exact Fisher-gauge algebra. It is to obtain the actual higher-window inputs and predeclare the process-aware uncertainty construction together with the existing scalar CMI and signed residual-orientation tests. That is an independent empirical step and belongs to a later invocation.
