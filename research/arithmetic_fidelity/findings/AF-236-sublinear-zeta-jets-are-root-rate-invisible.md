# AF-236 — sublinear zeta jets are invisible in the Li root-rate quotient

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `CLASSICAL-REPRESENTATION-SPECIALIZATION`, `RH-SUFFICIENT-QUOTIENT`, `TARGET-METRIC`, `NEGATIVE/OBSTRUCTION`, `INFORMATION-PRICE`, `NO-NOVELTY-CLAIM`

## Claim

AF-235 shows that the binary RH discriminator carried by the Li coefficients is only their exponential root-rate class modulo the vector space

\[
\mathcal S=\{a=(a_n):\limsup_{n\to\infty}|a_n|^{1/n}\le 1\}.
\tag{1}
\]

The standard local expansion of the zeta-dependent part of the Li coefficients gives a concrete information-price question for that quotient.

Put `w=s-1` and choose the analytic germ

\[
g(w)=\log\!\bigl(w\,\zeta(1+w)\bigr)
\tag{2}
\]

at `w=0`, normalized by `g(0)=0`. Write

\[
g'(w)=\frac1w+\frac{\zeta'}{\zeta}(1+w)
      =-\sum_{j\ge0}\eta_j w^j,
\tag{3}
\]

which defines the classical `eta_j` coefficients. The zeta-dependent Li contribution is the exact binomial transform

\[
Z_n
:=n[w^n](1+w)^{n-1}g(w)
=-\sum_{k=1}^n\binom nk\eta_{k-1}.
\tag{4}
\]

For any integer sequence `K_n` with `0<=K_n<=n`, define its depth-`K_n` local-jet truncation by

\[
Z_n^{\le K}
:=-\sum_{k=1}^{K_n}\binom nk\eta_{k-1}.
\tag{5}
\]

Then

\[
\boxed{
K_n=o(n)
\quad\Longrightarrow\quad
Z^{\le K}\in\mathcal S.
}
\tag{6}
\]

Consequently every fixed, slowly growing, or otherwise sublinear local zeta jet is **zero in the AF-235 RH-sufficient quotient**, independently of RH. If `Z_n^{>K}:=Z_n-Z_n^{\le K}`, then

\[
\boxed{
[\lambda]=[Z]=[Z^{>K}]
\quad\text{in }\mathbb C^{\mathbb N}/\mathcal S
\quad\text{for every }K_n=o(n).
}
\tag{7}
\]

Thus, within the canonical local-`eta` binomial reconstruction, any nonzero false-RH root-rate class must come from coefficient depths that are **not sublinear in the Li index**. A finite or `o(n)`-deep Taylor/derivative description at `s=1` cannot carry the AF-235 binary RH discriminator through this reconstruction, even when those retained coefficients are known exactly.

This is a target-relative information-price result. AF-235 permits enormous subexponential amplitude error, but that coarse tolerance does **not** make the target accessible from a shallow analytic jet: the Li transform can move exponentially small high-order local information into an exponentially visible global coefficient only when sufficiently deep orders are retained.

## Derivation

### The local zeta term is exactly a binomial jet transform

Since `w zeta(1+w)` is analytic and nonzero at `w=0`, `g` is analytic on some disk about the origin. From `(3)`,

\[
g(w)=-\sum_{k\ge1}\frac{\eta_{k-1}}{k}w^k.
\tag{8}
\]

For the Li differential functional applied to the zeta-dependent factor,

\[
\frac1{(n-1)!}
\left.\frac{d^n}{ds^n}
\left[s^{n-1}\log((s-1)\zeta(s))\right]\right|_{s=1}
=n[w^n](1+w)^{n-1}g(w).
\tag{9}
\]

Using `(8)`,

\[
\begin{aligned}
n[w^n](1+w)^{n-1}g(w)
&=-n\sum_{k=1}^n\frac{\eta_{k-1}}{k}
       \binom{n-1}{k-1}\\
&=-\sum_{k=1}^n\binom nk\eta_{k-1},
\end{aligned}
\tag{10}
\]

which is the classical `S_2(n)` / `eta`-binomial component appearing in the Li-coefficient literature.

### Analyticity gives only exponential coefficient cost

Because `g'` is analytic in a fixed neighborhood of `0`, Cauchy's estimate on any smaller circle gives constants `C>0` and `A>=1`, independent of `j`, such that

\[
|\eta_j|\le C A^j
\qquad(j\ge0).
\tag{11}
\]

No RH input is used here; this is local analyticity at the regular point `s=1` after the zeta pole has been cancelled.

Assume now `K_n=o(n)`. For all sufficiently large `n`, `K_n<n`. The standard binomial bound

\[
\binom nk\le\left(\frac{en}{k}\right)^k
\tag{12}
\]

and monotonicity of `k log(en/k)` for `1<=k<n` give

\[
|Z_n^{\le K}|
\le C K_n
\exp\!\left(
K_n\log\frac{en}{K_n}+K_n\log A
\right)
\tag{13}
\]

up to an immaterial fixed factor for the shift `k-1`. Put `alpha_n=K_n/n`. Then

\[
\frac1n\log^+|Z_n^{\le K}|
\le
\alpha_n\log\frac{eA}{\alpha_n}+o(1).
\tag{14}
\]

Since `alpha_n -> 0` and `alpha log(1/alpha) -> 0`, the right-hand side tends to zero. Therefore

\[
\limsup_{n\to\infty}|Z_n^{\le K}|^{1/n}\le1,
\tag{15}
\]

which proves `(6)`.

The conclusion is stronger than the fixed-jet obstruction. For example, depths `K_n=sqrt(n)`, `n/log n`, or `n/log log n` all remain invisible in the AF-235 quotient.

### The entire quotient class is in the deep zeta tail

Decompose the full Li coefficient as

\[
\lambda_n=A_n+Z_n,
\tag{16}
\]

where `A_n` is the explicit completion/archimedean contribution. AF-234 records the classical unconditional estimate `A_n=O(n log n)` at the precision needed here, so `A in S`. Hence AF-235 gives

\[
[\lambda]=[Z].
\tag{17}
\]

But `(6)` says `[Z^{\le K}]=0` for every sublinear depth. Since `Z=Z^{\le K}+Z^{>K}`,

\[
[\lambda]=[Z^{>K}],
\tag{18}
\]

proving `(7)`.

If RH is false, AF-235 gives `[lambda] != 0`; therefore the tail beyond every `o(n)` depth must carry that nonzero class. The conclusion is only a **necessary depth condition**. Retaining a linear fraction of the jet is not asserted to be sufficient, and no fixed fraction is claimed to be optimal.

## Why this is an Arithmetic Fidelity result

AF-235 changed the endpoint from exact Li coefficients or their `n log n` trend to the much coarser binary root-rate class. It might therefore appear that very little upstream information should be needed. Equation `(6)` shows why that inference is invalid.

The target metric is coarse in **amplitude** but expensive in **analytic depth**. Local Taylor coefficients of `g'` are individually controlled by ordinary analyticity; the binomial Li transform mixes depth with the growing index `n`. Every sublinear initial segment produces only subexponential output and is erased by the exact quotient that decides RH. The potentially decisive exponential signal is therefore a genuinely deep-jet phenomenon in this coordinate system.

This gives a concrete instance of a broader fidelity distinction from the line mandate: the amount of information that may be discarded at the **destination** does not determine how much structural depth must be retained at the **source** to reach that destination nontrivially.

## Matched controls and boundaries

**Finite-depth control.** If `K_n=K` is fixed, `(13)` is only polynomial in `n`, so fixed local derivative data are especially far below the root-rate threshold.

**Near-linear-but-sublinear control.** Even `K_n=n/log n` or `n/log log n` satisfies `(6)`. The obstruction is not merely that a fixed number of derivatives fails; every vanishing fraction of the available order fails in this exact binomial reconstruction.

**Linear-depth boundary.** The proof stops when `K_n/n` does not tend to zero. This identifies the first scale not ruled out by the entropy estimate, not a sufficient scale for RH detection. Cancellations, signs, and the actual `eta_j` structure may still make a linear-depth truncation subexponential.

**No arbitrary amplification.** The theorem concerns the canonical Li/`eta` binomial map `(5)`. An unrestricted decoder could take a shallow coefficient and artificially exponentiate it in `n`; that would not be the Li reconstruction and would require a separate intrinsicness and sufficiency argument.

**Exact coefficients, not finite precision.** The obstruction persists even if the retained local coefficients are known exactly. Bit complexity, numerical conditioning, and the precision needed to evaluate deep coefficients are separate information-price questions.

**Full-germ recovery is not contradicted.** The entire infinite analytic germ at `s=1` determines its local function and can be analytically continued where allowed. AF-236 concerns a growing sequence of finite truncations whose depth is sublinear relative to the Li index; it does not say the full analytic germ is non-faithful.

**Prime provenance is not the target.** The `eta_j` have arithmetic representations involving the von Mangoldt function, but `(6)` does not recover rational-prime provenance. Its target is only the AF-235 RH quotient.

## Prior art and novelty assessment

The ingredients around `(3)--(4)` are classical. Mark W. Coffey, **“New results concerning power series expansions of the Riemann xi function and the Li/Keiper constants,”** *Proceedings of the Royal Society A* 464 (2008), 711–731, DOI `10.1098/rspa.2007.0212`, explicitly develops the Laurent coefficients `eta_j` of `zeta'/zeta` at `s=1` and the alternating binomial component

\[
S_2(n)=-\sum_{k=1}^n\binom nk\eta_{k-1}
\]

inside the Li coefficients. That paper also gives von-Mangoldt and Stieltjes-constant representations for the local coefficients.

Coffey, **“Summation properties of the eta_j and Li constants,”** *Journal of Computational and Applied Mathematics* 233(3) (2009), 667–673, DOI `10.1016/j.cam.2009.02.034`, studies this same `eta`/Li connection and reduces RH to a growth condition on the full alternating binomial sum. Keiper's 1992 generating-function formulation and Voros's 2006 sharpened Li asymptotics supply the classical root-rate/RH endpoint already audited in AF-235.

No novelty is claimed for the Li differential identity, the `eta` expansion, the binomial transform, Cauchy coefficient bounds, or the classical RH criteria. A targeted literature search did not locate an explicit statement of the particular **sublinear truncation-depth obstruction** `(6)--(7)`. The Arithmetic Fidelity contribution is therefore the derived information-price organization: combining the classical local binomial representation with the AF-235 quotient proves that every `o(n)` local jet is automatically discarded by the exact binary RH endpoint.

## Evidence boundary

Equations `(6)` and `(7)` are exact consequences of local analyticity, the classical Li/`eta` binomial representation, elementary binomial estimates, and AF-234/AF-235. They do not assume RH.

The result does **not** prove that any linear-depth truncation detects RH, does not give a prime-side proof of the required deep-tail behavior, and does not show that deep local coefficients are easier to control than the zeros. It only rules out the entire sublinear-depth regime for this canonical reconstruction.

## Consequences for the research frontier

AF-235's next-step question can now be narrowed. A proposed prime-side or local-analytic surrogate for the Li root-rate endpoint should not be judged only by its additive error magnitude; it must also be audited for the **depth at which the exponential class can first enter**.

For the classical local zeta expansion, any route that computes or controls only `o(n)` `eta` coefficients for the `n`th Li observable is dead at the AF-235 quotient level. The next useful question is whether a natural linear-scale aggregation of the `eta`/von-Mangoldt data admits a coarser sufficient statistic, cancellation theorem, or alternate representation that controls the root-rate class without reconstructing the full Li coefficient sequence.