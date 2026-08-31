# WI-058 — the `W`-local pair main has exponentially tight Fourier-conductor energy

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + LITERATURE+DERIVED + PRIOR-ART-REDIRECTION`. This finding does **not** certify the Yang--Yang one-sided fourth-moment candidate, enlarge the Shao--Teräväinen region of WI-054, or change Mathia's current unconditional simple-critical proportion. It narrows the conditioned-pair obstruction isolated in WI-057.

The `W`-local all-main pair is periodic modulo the primorial `W=P(w)`, which can make the conditioning problem look as though a repair must control arbitrary frequencies at the full `W` scale. That is too pessimistic in `L^2`. After normalizing the pair main to mean one on `Z/WZ`, its squared Fourier coefficients have an exact product law: for every active local prime `p`, the event that a Fourier character's conductor contains `p` is independent across primes and has probability

\[
\boxed{
\theta_p(h)=
\begin{cases}
1/p,&p\mid h,\\[1mm]
2/p,&p\nmid h.
\end{cases}}
\tag{1}
\]

For locally admissible shifts this gives the uniform conductor tail

\[
\boxed{
\nu_{W,h}\{\operatorname{cond}>w^K\}\ll e^{-K},
}
\tag{2}
\]

where `nu_{W,h}` is the probability measure obtained by normalizing the squared Fourier coefficients. Moreover the total `L^2` energy of the normalized pair main is `O((log w)^2)`. Hence projecting onto characters of conductor at most

\[
D_w:=w^{3\log\log w}
\tag{3}
\]

leaves an **absolute** squared-`L^2` tail `O(1/log w)=o(1)`. At the Shao--Teräväinen choice `w=(log X)^C`,

\[
\boxed{
D_w
=\exp\!\bigl(O(\log\log X\,\log\log\log X)\bigr)
=X^{o(1)}.
}
\tag{4}
\]

Thus the local periodic modes exposed by WI-057 are spectrally concentrated on subpolynomial conductors, despite the full period `W` being vastly larger. This is a real reduction of the missing theorem interface, but not its solution: one still needs a source-normalized conditioned/twisted shifted-prime estimate, or an equivalent square-function estimate, that can pair the **actual prime-pair error** against these modes without reintroducing the WI-042 family Cauchy floor. Conductor truncation alone does not supply that orthogonality.

## 1. Source interface and scope

The relevant literature input is the same one already audited in WI-054 and WI-057.

Shao--Teräväinen, *The Bombieri--Vinogradov theorem for nilsequences* (Discrete Analysis 2021:21, arXiv:2006.05954v2), Theorem 1.3, compares `Lambda` on progressions with the explicit small-prime model

\[
\frac{dW}{\varphi(dW)}1_{(n,W)=1},
\qquad
W=P((\log x)^C).
\tag{5}
\]

MRT's local-factor discussion writes the corresponding prime factor as

\[
\Lambda_p(n)=\frac{p}{p-1}1_{p\nmid n}.
\tag{6}
\]

WI-057 showed that when one pair is replaced by its `W`-local all-main model, the product of two factors (6) retains nonconstant residue modes; ordinary unweighted MRT control of the other pair is therefore insufficient. The present question is narrower: **how arithmetically complicated is the spectrum of that deterministic `W`-local pair itself?**

Fix

\[
W=\prod_{p\le w}p
\tag{7}
\]

and a shift `h` for which the local pair main is nonzero. In particular `h` is even when `2|W`; if a local obstruction makes the pair main identically zero, there is no normalized all-main conditioning object to estimate and the theorem below is simply not invoked. Define

\[
F_{W,h}(n)
:=
\prod_{p\le w}\Lambda_p(n)\Lambda_p(n+h),
\qquad n\in\mathbb Z/W\mathbb Z,
\tag{8}
\]

and normalize

\[
G_{W,h}:=\frac{F_{W,h}}{\mathbb E_{n\bmod W}F_{W,h}},
\qquad
\mathbb E G_{W,h}=1.
\tag{9}
\]

If a progression condition pins an admissible local coordinate at a prime dividing its modulus, that local factor becomes constant and can simply be deleted from the active product. All bounds below therefore remain valid, and the exact law applies to the remaining active primes.

## 2. Exact one-prime energy

Put

\[
F_{p,h}(n):=\Lambda_p(n)\Lambda_p(n+h)
\qquad(n\bmod p).
\tag{10}
\]

There are two cases.

If `p|h`, the two forbidden residues coincide. Then

\[
\mathbb E F_{p,h}=\frac p{p-1},
\qquad
G_{p,h}(n)
=\frac p{p-1}1_{p\nmid n},
\tag{11}
\]

and therefore

\[
\mathbb E|G_{p,h}|^2=\frac p{p-1},
\qquad
v_p:=\mathbb E|G_{p,h}|^2-1=\frac1{p-1}.
\tag{12}
\]

If `p` does not divide `h`, there are two distinct forbidden residues (this case can occur only for `p>=3` under local admissibility). Thus

\[
\mathbb E F_{p,h}=\frac{p(p-2)}{(p-1)^2},
\qquad
G_{p,h}(n)
=\frac p{p-2}1_{p\nmid n(n+h)},
\tag{13}
\]

so

\[
\mathbb E|G_{p,h}|^2=\frac p{p-2},
\qquad
v_p=\frac2{p-2}.
\tag{14}
\]

Use normalized finite Fourier transform. Since every `G_{p,h}` has mean one, its zero Fourier coefficient is exactly `1`. Parseval says that the **total** squared mass of all nonzero local Fourier coefficients is exactly `v_p`.

No estimate has entered yet.

## 3. CRT makes the Fourier support a product probability law

The Chinese remainder identification

\[
\mathbb Z/W\mathbb Z
\cong
\prod_{p\le w}\mathbb Z/p\mathbb Z
\tag{15}
\]

turns (9) into the tensor product

\[
G_{W,h}=\bigotimes_{p\le w}G_{p,h}.
\tag{16}
\]

The finite Fourier transform respects this tensor product. For a character `a mod W`, write

\[
d(a):=\frac{W}{(a,W)},
\tag{17}
\]

with `d(0)=1`. Because `W` is squarefree, `p|d(a)` exactly when the local `p`-component of the character is nonzero.

Normalize squared Fourier mass to a probability measure

\[
\nu_{W,h}(a)
:=
\frac{|\widehat G_{W,h}(a)|^2}
{\sum_{b\bmod W}|\widehat G_{W,h}(b)|^2}.
\tag{18}
\]

At a fixed prime, the zero-frequency mass is `1` and the aggregate nonzero-frequency mass is `v_p`. Therefore under (18) the indicator

\[
I_p(a):=1_{p\mid d(a)}
\tag{19}
\]

is Bernoulli with parameter

\[
\theta_p=\frac{v_p}{1+v_p}.
\tag{20}
\]

Equations (12) and (14) give exactly

\[
\boxed{
\theta_p=
\begin{cases}
1/p,&p\mid h,\\[1mm]
2/p,&p\nmid h.
\end{cases}}
\tag{21}
\]

and the indicators `(I_p)_{p<=w}` are independent because the squared Fourier weights tensorize. This proves (1). Notice that the individual nonzero frequencies at one prime need not have equal weights; only their aggregate mass matters, and that is all the conductor event records.

## 4. Exponential tail for the Fourier conductor

Under `nu_{W,h}`,

\[
d(a)=\prod_{p\le w}p^{I_p(a)}.
\tag{22}
\]

For `s>0`, independence gives

\[
\mathbb E_\nu d^s
=
\prod_{p\le w}
\left(1+\theta_p(p^s-1)\right).
\tag{23}
\]

Since `theta_p<=2/p`,

\[
\mathbb E_\nu d^s
\le
\exp\left(
2\sum_{p\le w}\frac{p^s-1}{p}
\right).
\tag{24}
\]

Take

\[
s=\frac1{\log w}.
\tag{25}
\]

For `p<=w`, `0<=log p/log w<=1`, so convexity of the exponential on `[0,1]` gives

\[
p^s-1
=e^{\log p/\log w}-1
\le
(e-1)\frac{\log p}{\log w}.
\tag{26}
\]

The classical Mertens estimate

\[
\sum_{p\le w}\frac{\log p}{p}
=\log w+O(1)
\tag{27}
\]

therefore makes (24) uniformly bounded as `w->infinity`:

\[
\mathbb E_\nu d^{1/\log w}\ll1.
\tag{28}
\]

Markov's inequality now yields, for every `K>=0`,

\[
\boxed{
\nu_{W,h}\{d>w^K\}
\le
w^{-K/\log w}
\mathbb E_\nu d^{1/\log w}
\ll e^{-K}.
}
\tag{29}
\]

The implied constant is absolute after enlarging it to cover bounded `w`, and the estimate is uniform in every locally admissible `h`.

This is stronger than an expectation statement: it is an exponential large-deviation bound for the exact Fourier-energy conductor distribution.

## 5. The absolute `L^2` tail is subpolynomial-conductor

The normalized pair main itself has

\[
\|G_{W,h}\|_2^2
=
\prod_{p\le w,\ p\mid h}\frac p{p-1}
\prod_{p\le w,\ p\nmid h}\frac p{p-2},
\tag{30}
\]

where the second product only contains `p>=3`. Since

\[
\frac p{p-1}\le\frac p{p-2}
\qquad(p\ge3),
\tag{31}
\]

Mertens' theorem gives the uniform bound

\[
\boxed{
\|G_{W,h}\|_2^2\ll(\log w)^2.
}
\tag{32}
\]

Indeed `log(p/(p-2))=2/p+O(1/p^2)` for `p>=3`; the `p=2` factor is an absolute constant.

Let `Pi_{<=D}` be the orthogonal Fourier projection onto characters with conductor `d(a)<=D`. Equations (18), (29), and Parseval give

\[
\boxed{
\|(1-\Pi_{\le w^K})G_{W,h}\|_2^2
\ll
(\log w)^2e^{-K}.
}
\tag{33}
\]

Choose `K=3 log log w`. Then

\[
\boxed{
\|(1-\Pi_{\le D_w})G_{W,h}\|_2^2
\ll\frac1{\log w}=o(1),
\qquad
D_w=w^{3\log\log w}.
}
\tag{34}
\]

If `w=(log X)^C`, as in the Shao--Teräväinen `W`-local model, then

\[
\log D_w
=3\log w\log\log w
=O(\log\log X\log\log\log X),
\tag{35}
\]

which proves (4).

The factor `3` is not optimized and has no intrinsic meaning. More generally, any `K=(2+eta)log log w` gives a vanishing squared-`L^2` tail. The durable point is the scale `exp(O(log w log log w))`, not the displayed constant.

## 6. What this changes after WI-057

WI-057 proves an information-interface no-go: even perfect **marginal interval discrepancy** for one shifted-pair error does not imply orthogonality to the periodic modes carried by the other `W`-local pair. That conclusion remains intact.

The present result removes a stronger pessimistic interpretation. The conditioning sigma-algebra is periodic modulo `W`, but its `L^2` spectrum is not spread uniformly across `W`-scale conductors. Up to `o(1)` absolute local-main `L^2` energy, it is carried by characters whose individual conductors are only

\[
X^{o(1)}.
\tag{36}
\]

Consequently a future one-sided repair does **not** intrinsically need a pair-correlation theorem uniform for arbitrary twists of conductor comparable to the full primorial. A source-faithful target can instead try to prove conditioned/twisted shifted-prime control for the low-conductor spectrum and dispose of the high-conductor local-main tail in a compatible Hilbert-space norm.

This is a materially smaller arithmetic interface than “control every `W`-periodic mode.” It is also distinct from WI-052: BDH removes the pure residue-class-constant quotient projection of a **single prime residual** on power-separated moduli, whereas (29)--(34) describe the deterministic small-prime spectrum of the **pair all-main weight** that WI-057 showed can still couple to the opposite pair error.

## 7. Why this does not yet enlarge the analytic region

There are three non-negotiable gaps between (34) and a Yang welding theorem.

First, `Pi_{<=D}` is a sum of many characters of individually small conductor; it is not one periodic function of a single modulus `<=D`. A proof must keep an `ell^2`/square-function structure or another summation mechanism and may not pay the forbidden across-family Cauchy loss of WI-042.

Second, (34) controls the norm of the **deterministic local main**, not the norm of the opposite shifted-prime error. To estimate their covariance by Cauchy--Schwarz, one needs a source-normalized bound on the companion pair-error norm strong enough that the `o(1)` local-main tail remains `o(1)` after all Yang weights and collars are restored.

Third, ordinary MRT still does not provide the required low-conductor twisted statement. WI-057's parity example is already a conductor-`2` obstruction. Thus reducing the spectrum to subpolynomial conductor does not make marginal MRT sufficient; it only sharpens what an extension of MRT, a circle-method refinement, or a source-specific dispersion theorem would have to control.

Accordingly WI-054's established region remains

\[
4\alpha+\beta<1,
\qquad
\alpha+4\beta<1,
\tag{37}
\]

with fixed margins. No one-sided union is claimed here.

## 8. Prior-art and novelty audit

No novelty is claimed for the `W`-trick, the local prime factor (6), finite Fourier analysis on cyclic groups, Parseval, CRT tensorization, Mertens' estimate (27), or Rankin/Markov tail bounds. The W-local prime approximant is explicit in Shao--Teräväinen 2021 and in the later higher-uniformity literature; MRT's local-factor language is already the source used by WI-057. Ramanujan/Fourier decompositions of coprimality indicators are classical harmonic-analysis facts.

A targeted search around W-tricked prime models, Fourier/Ramanujan expansions of coprimality indicators, primorial wheels, and small-prime local factors found the expected classical ingredients but no theorem in the cited Yang/MRT/Shao--Teräväinen chain that states the exact Bernoulli conductor law (21) or uses the tail (29) to formulate the conditioned welding interface. That absence is **not** a priority claim.

The Mathia contribution recorded here is the source-specific exact deduction: normalize the precise pair local main relevant to WI-057, compute its one-prime nonzero Fourier energy, tensor it through CRT, and turn the resulting Bernoulli support law into the subpolynomial effective-conductor reduction (34)--(35).

## 9. Decisive audit and continuation gate

Narrow or withdraw this finding if any of the following fails.

1. Recompute the local means (11), (13) and the Parseval energies (12), (14), including the locally obstructed `p=2` case.
2. Verify that the Yang/ST all-main pair factorizes over active primes exactly as in (8) after any progression coordinates pinned by the coefficient modulus are removed.
3. Verify that global normalized Fourier coefficients tensorize under CRT and that `d(a)=W/(a,W)` records exactly the set of nonzero local character coordinates.
4. Reproduce the exact probabilities `1/p` and `2/p` from `v/(1+v)`; no equidistribution assumption on the individual nonzero local frequencies is allowed.
5. Recheck the Mertens/Markov derivation (23)--(29) and the absolute-energy conversion (30)--(34).
6. Do **not** infer a low-conductor twisted pair theorem from this deterministic spectral truncation. The next substantive step must prove the source-normalized covariance estimate against the retained characters, together with a norm bound that makes the discarded tail harmless.

The sharpened live question is therefore

\[
\boxed{
\text{can the post-local-main shifted-prime pair error be controlled}
\text{ against the }X^{o(1)}\text{-conductor spectrum in (34),}
\text{ with source weights and no WI-042 family-Cauchy floor?}
}
\tag{38}
\]

A positive answer would materially strengthen the one-sided fourth-moment route. A counterexample or theorem barrier showing that even this subpolynomial-conductor conditioned interface is out of reach would close another important repair family.