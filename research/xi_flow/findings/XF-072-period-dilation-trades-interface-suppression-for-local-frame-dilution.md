# XF-072 — period dilation trades interface suppression for local frame dilution

**Status:** `EXACT-DERIVED` + `MATCHED-CONTROL` + `NEGATIVE/OBSTRUCTION` + `LOCALIZATION/FRAME-TRADEOFF`. XF-069 identifies the center-averaged mismatch between the actual Xi selector and a periodic surrogate as the remaining source-side localization burden, while XF-070--XF-071 show that the selector-induced weighted log-Vieta quotient is exactly the resource that must be transported. A natural attempted repair is to periodize a much larger block: move the artificial seam farther from the transition window, so only a small fraction of translated centers see the boundary.

That repair has an exact normalization obstruction. If the periodic block length is

\[
N=RM
\tag{1}
\]

instead of the fixed choice `N=2M`, then the full-period center Parseval identity remains exact, but its local `H^3` frame constant is reduced by precisely the same factor `1/R` as the fraction of centers exposed to one seam. Thus enlarging the period suppresses boundary exposure only by diluting the transition signal at the same rate. Renormalizing the center average by `R` to retain an order-one local frame removes the apparent gain.

A one-point seam control makes the obstruction quantitative. Let the periodic surrogate be the integer lattice and let the nonperiodic continuation agree with all `N` representatives `0,1,...,N-1` but omit the next point `N`. The two configurations agree exactly on the whole chosen block, their global counting functions differ by at most one, and all gaps are `1` except a single gap `2`. Nevertheless the weighted center-averaged interface resource on the XF-059 slow cone is

\[
\boxed{
\mathfrak I_{T,R}
=\frac{G_R}{R}\,
M^3\int_{B_T}\theta^4\,d\theta,
\qquad
G_R:=\int_0^R|g(u)|^2\,du>0.
}
\tag{2}
\]

For `M=q^2` and

\[
B_T=
\left[q^{-2+\delta},\frac{C\log\log T}{q}\right],
\qquad 0<\delta<1,
\tag{3}
\]

this becomes

\[
\boxed{
\mathfrak I_{T,R}
=\frac{G_R C^5}{5R}\,
q(\log\log T)^5\,(1+o(1)).
}
\tag{4}
\]

Hence a fixed aspect ratio gives a large interface error, while the local-frame normalization `R\mathfrak X` gives

\[
\boxed{
R\mathfrak I_{T,R}
=G_RM^3\int_{B_T}\theta^4\,d\theta,
}
\tag{5}
\]

which does not improve with period dilation and in the source cone grows like `q(log log T)^5` whenever `R` stays bounded away from zero or tends to infinity. The obstruction is not that large-period periodization is useless; it is that **full-period averaging cannot simultaneously make a generic seam negligible and retain order-one coercivity for one local transition block by aspect-ratio enlargement alone**.

This does not rule out an Xi-specific interface theorem. It says that such a theorem must exploit more than seam distance plus the local counting/gap envelopes already admitted in the periodic model, or else replace the exact full-period Parseval architecture by a genuinely different center-local construction and pay its new localization/conditioning error.

## 1. Exact center Fourier extraction for arbitrary aspect ratio

Let

\[
x_{j+N}=x_j+N,
\qquad N=RM,
\tag{6}
\]

and use the same XF-056--XF-071 bandlimited envelope

\[
\chi=\widehat g\in C_c^\infty((-1,1)),
\qquad
C_g:=\int_{\mathbb R}|\chi(u)|^2\,du>0.
\tag{7}
\]

For a translated center `r`, define

\[
\mathcal S_r(\theta)
:=
\sum_{j\in\mathbb Z}
 g\!\left(\frac{x_j-r}{M}\right)
 e^{-i\theta(x_j-r)}.
\tag{8}
\]

Put

\[
\xi_k:=\frac{2\pi k}{N},
\qquad
P_k:=\sum_{j=0}^{N-1}e^{-i\xi_kx_j}.
\tag{9}
\]

The calculation of XF-069 does not use `N=2M`. For arbitrary `N`, it gives exactly

\[
\boxed{
\frac1N\int_0^N
\mathcal S_r(\theta)e^{-i\xi_kr}\,dr
=
\frac{M}{N}
\chi\!\bigl(M(\theta-\xi_k)\bigr)P_k.
}
\tag{10}
\]

Thus increasing the period does move the seam farther away in physical center, but the exact Fourier coefficient carrying one Vieta power sum is simultaneously reduced from `1/2` to `1/R`.

## 2. General center Parseval has an exact `1/R` tangent frame

For a measurable positive-frequency set `B`, keep the selector norm of XF-070,

\[
\|F\|_{X(B)}^2
:=M^3\int_B\theta^4|F(\theta)|^2\,d\theta,
\tag{11}
\]

and define the full-period center average

\[
\mathfrak X_B^{(R)}
:=
\frac1N\int_0^N
\|\mathcal S_r\|_{X(B)}^2\,dr.
\tag{12}
\]

Parseval in `r` applied to (10) gives the exact identity

\[
\boxed{
\mathfrak X_B^{(R)}
=
\sum_{k\in\mathbb Z}
 w_{k,B}^{(R)}|P_k|^2,
}
\tag{13}
\]

where

\[
\boxed{
 w_{k,B}^{(R)}
=
\frac{M^4}{N^2}
\int_{U_{k,B}}
\left(\xi_k+\frac uM\right)^4
|\chi(u)|^2\,du
=
\frac1{R^2M^2}
\int_{U_{k,B}}
\left(\frac{2\pi k}{R}+u\right)^4
|\chi(u)|^2\,du,
}
\tag{14}
\]

and

\[
U_{k,B}
:=
\left\{
 u\in\operatorname{supp}\chi:
 \xi_k+\frac uM\in B
\right\}.
\tag{15}
\]

No disjoint-sideband assumption is needed for (13): orthogonality is in the translated-center variable. If the whole sideband of `\xi_k` lies in `B` and `M|\xi_k|\to\infty`, then uniformly on the slow cone

\[
\boxed{
 w_{k,B}^{(R)}
=
\frac{C_gM^2}{R^2}\,
\xi_k^4(1+o(1)).
}
\tag{16}
\]

Now linearize around the arithmetic lattice,

\[
x_j=j+\varepsilon a_j,
\qquad a_{j+N}=a_j,
\tag{17}
\]

with unitary DFT

\[
\widehat a_k
=N^{-1/2}\sum_{j=0}^{N-1}a_je^{-i\xi_kj}.
\tag{18}
\]

For nonzero `k`, the unperturbed power sum vanishes and

\[
\left.
\frac d{d\varepsilon}P_k
\right|_{0}
=-i\xi_k\sqrt N\,\widehat a_k.
\tag{19}
\]

Combining (16), (19), and `N=RM` gives one positive-frequency mode the asymptotic selector weight

\[
\boxed{
 w_{k,B}^{(R)}
\left|
\left.\frac d{d\varepsilon}P_k\right|_0
\right|^2
=
\frac{C_g}{R}
M^3\xi_k^6|\widehat a_k|^2(1+o(1)).
}
\tag{20}
\]

On the shrinking Xi slow cone, `|e^{i\xi}-1|^6=\xi^6(1+o(1))`. Therefore for a real tangent, whose positive and negative Fourier energies agree,

\[
\boxed{
\mathfrak X_{B}^{(R),\mathrm{lin}}(a)
=
\left(\frac{C_g}{2R}+o(R^{-1})\right)
\mathcal Q_M(B\cup(-B);a),
}
\tag{21}
\]

where `\mathcal Q_M` is the XF-062 third-difference `H^3` energy. Setting `R=2` recovers the `C_g/4` frame coefficient of XF-063. This is a useful consistency check and shows that the aspect-ratio loss is not an artifact of a new normalization.

Equation (21) is the first half of the tradeoff: a local transition state carrying a fixed amount of `\mathcal Q_M` is diluted by `1/R` when measured through the normalized full-period center average. Multiplying the resource by `R` is the natural way to preserve the local frame constant.

## 3. One omitted exterior point gives an exact seam mismatch

The second half needs no asymptotics. Take the periodic surrogate

\[
X^{\rm per}=\mathbb Z,
\tag{22}
\]

which is generated by the representatives `0,1,...,N-1`, and compare it with the nonperiodic configuration

\[
X^{\rm seam}
:=
\mathbb Z\setminus\{N\}.
\tag{23}
\]

The two configurations agree exactly on every representative used to construct the periodic block. Globally, their counting functions differ by at most one. The gaps of `X^{seam}` are all `1` except for the single gap from `N-1` to `N+1`, which has length `2`. Thus the control obeys substantially stronger density information than the coarse source-counting tolerances used in the local Xi comparisons; its only defect is the continuation across one artificial seam.

Because the two point measures differ by exactly one atom, their selector difference is exactly

\[
\boxed{
\Delta\mathcal S_r(\theta)
:=
\mathcal S_r^{\rm per}(\theta)
-
\mathcal S_r^{\rm seam}(\theta)
=
 g\!\left(\frac{N-r}{M}\right)
 e^{-i\theta(N-r)}.
}
\tag{24}
\]

Hence, with the same weighted source norm,

\[
\begin{aligned}
\mathfrak I_B^{(R)}
&:=
\frac1N\int_0^N
\|\Delta\mathcal S_r\|_{X(B)}^2\,dr\\
&=
M^3\int_B\theta^4\,d\theta
\cdot
\frac1N\int_0^N
\left|g\!\left(\frac{N-r}{M}\right)\right|^2dr\\
&=
\boxed{
\frac{G_R}{R}
M^3\int_B\theta^4\,d\theta,
}
\end{aligned}
\tag{25}
\]

with

\[
G_R:=\int_0^R|g(u)|^2\,du.
\tag{26}
\]

Since `g` is the nonzero inverse Fourier transform of a compactly supported smooth function, it cannot vanish on an interval; thus `G_R>0` for every `R>0`. If `R\to\infty`, then `G_R` increases to the positive half-line mass `\int_0^\infty|g(u)|^2du`.

The seam exposure therefore has exactly the same `1/R` factor as the tangent frame in (21).

## 4. On the Xi source cone the renormalized seam cost does not decrease

Use the source scales of XF-059--XF-071,

\[
M=q^2,
\qquad
B_T=
\left[
q^{-2+\delta},
\frac{C\log\log T}{q}
\right],
\qquad
0<\delta<1.
\tag{27}
\]

Then

\[
\begin{aligned}
M^3\int_{B_T}\theta^4\,d\theta
&=
\frac{q^6}{5}
\left[
\frac{C^5(\log\log T)^5}{q^5}
-q^{-10+5\delta}
\right]\\
&=
\boxed{
\frac{C^5}{5}
q(\log\log T)^5(1+o(1)).
}
\end{aligned}
\tag{28}
\]

Substitution in (25) proves (4). If one lets `R` grow, the unrenormalized seam resource can indeed be reduced by the small boundary fraction `1/R`. But equation (21) says that the desired local transition signal is reduced by the same `1/R`. Restoring an `R`-independent local frame multiplies both sides by `R`, and the seam control becomes

\[
\boxed{
R\mathfrak I_{B_T}^{(R)}
=
\frac{C^5G_R}{5}
q(\log\log T)^5(1+o(1)).
}
\tag{29}
\]

There is therefore no aspect-ratio choice inside the **full-period normalized center-Parseval architecture** that makes this admitted seam control negligible while keeping a fixed local `H^3` frame constant.

The conclusion is stronger than the statement that a hard seam is aesthetically undesirable. The same center normalization that makes distant seams occupy a small measure also averages a single local transition block over the enlarged period. Period length is not a free localization resource once the target is a local coercive quantity.

## 5. Stress tests and boundaries

The missing-point control is deliberately static. It is not claimed to be an Xi zero set or a heat-flow trajectory, and it does not contradict the actual prime-free selector theorem. Its role is falsificatory: **local agreement on the whole periodizing block, bounded gaps, and even `O(1)` global counting discrepancy are insufficient to make the weighted interface small.** Any proof that uses only such information cannot establish the XF-071 source hypothesis after period dilation.

The result also does not rule out taking `R\to\infty` for another purpose. If one is willing to accept the `1/R` loss in local coercivity, a larger period genuinely reduces the normalized seam exposure. The obstruction is specifically to using period dilation as a free way to obtain both negligible interface and an order-one single-block frame.

Nor does this exclude a center scan restricted to a deep interior subinterval of length `O(M)`. Such a scan can keep the seam many window widths away without averaging the local signal over all `N` centers. But then the exact Fourier orthogonality in (10)--(13) is lost: one no longer extracts individual periodic Vieta modes by a full-period Fourier coefficient. A successful interior-scan construction would therefore be a genuinely new localization theorem, not a consequence of simply increasing `N` in XF-069.

Likewise, Xi-specific analytic cancellation can still defeat the matched seam control. The actual moving-line selector is rapidly small because of the explicit-formula frequency gap, a property not shared by (23). A valid interface theorem may exploit that global analytic structure to cancel or absorb the continuation defect. XF-072 only shows that generic density/envelope information plus geometric seam distance cannot do the job.

## 6. Prior-art and novelty boundary

Boundary and wrap-around effects created by periodizing nonperiodic data are classical in Fourier analysis, windowed Fourier methods, and circulant approximations. The use of a smooth window to suppress such effects is also standard. The periodic backward-heat setting itself is already anchored in the Kabluchko source listed in `research/xi_flow/SOURCES.md`. No novelty is claimed for any of those general facts.

The line-specific contribution is the exact **aspect-ratio cancellation** in the Mathia selector/Vieta normalization: equations (20)--(21) show that the local third-difference frame constant is `Theta(R^{-1})`, while the explicit seam control (24)--(25) has the same `Theta(R^{-1})` center-average cost. A targeted prior-art audit found general results on windowed approximation of nonperiodic functions and circulant/periodization boundary effects, but no statement matching this de Bruijn--Newman selector normalization or its `M^3 theta^4` / Vieta `H^3` resource. The proof is self-contained and adds no load-bearing literature dependency, so `SOURCES.md` is unchanged.

## 7. Consequence for `xi_flow`

XF-071 reduces the periodic algebraic transport problem to a source-side center-averaged weighted Xi-to-periodic interface estimate plus a transition-side nontriviality theorem. XF-072 rules out the most direct geometric attempt to remove the first burden: **making the periodic block arbitrarily larger does not buy interface smallness at fixed local coercivity.**

The source bridge must therefore do one of two genuinely new things. It can exploit Xi-specific analytic cancellation across the artificial continuation while retaining full-period Vieta extraction, or it can replace full-period center Parseval by an interior/localized center transform and control the resulting mode-mixing/conditioning error. Merely enlarging the period and appealing to a smaller seam fraction cannot close the bridge.

This is a structural restriction on the present route, not an upper bound on `Lambda`. It does not prove that the actual Xi interface mismatch is large, does not produce a positive-`Lambda` transition state, and does not alter the exact guarded transport theorem of XF-071.