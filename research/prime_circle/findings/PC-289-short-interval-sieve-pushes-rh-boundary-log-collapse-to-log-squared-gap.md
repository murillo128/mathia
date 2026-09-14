# PC-289 — short-interval sieve pushes RH boundary-log collapse to a log-squared gap

**Status:** `LITERATURE+DERIVED` + `CONDITIONAL-RH-COROLLARY` + `DECISIVE-BOUNDARY` for the exact one-profile boundary-log finite-section frontier left by PC-288.

PC-287 controls the clipping error of the exact selector-subtracted boundary logarithm by combining the discrete square sum of the clipped log singularity with the **maximum atom** of the source. Since the normalized prime source has atoms of size `asymp (log q)/q`, this gives the term

\[
\sqrt{\varepsilon\log q+\frac{(\log q)^3}{q}}.
\]

PC-288 then sharpens only the transport side, replacing the global Lipschitz cost by one-dimensional spectral-path variation. Its resulting RH classicalization range is

\[
B=o\!\left(\frac{\sqrt q}{(\log q)^{5/2}}\right).
\]

The factor `log q` in the clipping mass is not intrinsic. For a noncentral matrix entry, fixing one source coordinate turns the small-phase condition into a union of short intervals for the other prime coordinate. A classical Brun--Titchmarsh-type upper bound on primes in arbitrary intervals shows that every logarithmic-depth band above a very small tail carries mass proportional to its **arc length**, not arc length times the maximal prime atom. The remaining deep tail is so short that the crude atom bound is harmless.

Put `L=log q`. For the same exact matrix, same flat clipping, same prime source, same denominator-`q` Li-grid control, and same normalized ordered singular-spectrum law as PC-287/PC-288, one obtains the sharper deterministic estimate

\[
\boxed{
W_1^{(\ell^\infty)}\!\left(
\rho^{prime,log}_{q,B},
\rho^{Li,log}_{q,B}
\right)
\ll
\sqrt{\varepsilon+\frac{L^3}{q}}
+\frac{B}{\sqrt\varepsilon}\,\Delta_q
+\frac{L^2}{q},
}
\tag{1}
\]

whenever `q` is prime, `N=2B+1<=q`, `1/q<=epsilon<=1/4`, and

\[
\boxed{
\frac{\varepsilon q}{B}\ge q^{1/3}
}
\tag{2}
\]

for all sufficiently large `q`. Here

\[
\Delta_q
=
\sup_{0\le t\le1}
\left|\nu_q([0,t])-\widetilde\lambda_q([0,t])\right|
\]

is exactly the source Kolmogorov discrepancy of PC-288.

Under RH, PC-288 gives

\[
\Delta_q\ll q^{-1/2}L^2+\frac{L}{q}.
\tag{3}
\]

Choosing

\[
\boxed{
\varepsilon_q:=Bq^{-1/2}L^2
}
\tag{4}
\]

then satisfies (2) automatically, since `epsilon_q q/B=q^{1/2}L^2`, and gives

\[
\boxed{
W_1^{(\ell^\infty)}\!\left(
\rho^{prime,log}_{q,B},
\rho^{Li,log}_{q,B}
\right)
\ll
B^{1/2}q^{-1/4}L
+B^{1/2}q^{-3/4}
+\frac{L^{3/2}}{\sqrt q}
+\frac{L^2}{q}.
}
\tag{5}
\]

Consequently,

\[
\boxed{
\mathrm{RH}
\quad\Longrightarrow\quad
B=o\!\left(\frac{\sqrt q}{(\log q)^2}\right)
\quad\Longrightarrow\quad
W_1^{(\ell^\infty)}\!\left(
\rho^{prime,log}_{q,B},
\rho^{Li,log}_{q,B}
\right)\to0.
}
\tag{6}
\]

This removes another half power of `log q` from the proven RH-forced classicalization boundary. The remaining `log^2 q` gap now comes from the pointwise RH prime-to-Li source discrepancy (3), rather than from charging the logarithmic clipping region by the worst source atom.

## 1. Small phase preimages are unions of genuinely long prime intervals

Retain the PC-287 clipping difference

\[
\delta_{q,\varepsilon}(t)
:=k_q(t)-g_\varepsilon(t/q),
\qquad t\in\mathbb Z/q\mathbb Z,
\tag{7}
\]

with

\[
|\delta_{q,\varepsilon}(t)|
\ll 1+\log\frac{\varepsilon q}{|t|_q}
\quad(1\le |t|_q<\varepsilon q),
\tag{8}
\]

and `|delta_{q,epsilon}(0)|<<L`.

Fix a nonzero integer `a` with `1<=|a|<=B` and a residue `c mod q`. For an integer radius `1<=u<=q/4`, the condition

\[
|ap+c|_q\le u
\tag{9}
\]

on `2<=p<=q` is the intersection of the prime set with a union of `O(|a|+1)` ordinary real intervals. Each nonempty interior interval has length

\[
\asymp \frac{u}{|a|},
\tag{10}
\]

and the total interval length is `O(u)`.

Ramaré and Schlage-Puchta prove a uniform sieve bound for primes in an arbitrary interval of length `H`, namely

\[
\pi(M+H)-\pi(M)\ll \frac{H}{\log H}
\tag{11}
\]

for sufficiently large `H`, uniformly in the interval position. Their explicit theorem is stronger: `pi(M+H)-pi(M)<=2H/(log H+3.53)` once `H` is large enough. Therefore, whenever

\[
\frac{u}{|a|}\ge q^{1/6},
\tag{12}
\]

the union in (9) contains

\[
\ll \frac{u}{L}
\tag{13}
\]

primes. Since the normalized prime source has `asymp q/L` atoms,

\[
\boxed{
\nu_q\{p/q:|ap+c|_q\le u\}
\ll \frac{u}{q}.
}
\tag{14}
\]

The same estimate holds for the denominator-`q` Li-grid control `widetilde lambda_q`. Before grid projection, an integer interval of length `H>=q^{1/6}` has normalized Li mass

\[
\ll
\frac{H/\log H}{q/L}
\ll \frac{H}{q}.
\tag{15}
\]

Nearest-grid projection enlarges each of the `O(|a|)` preimage intervals by only `O(1)` grid cells. Under (12), `|a|<=u q^{-1/6}`, while PC-287 gives maximal Li-grid atom `O(L/q)`; hence the total projection padding is `O(uL/(q q^{1/6}))=o(u/q)`. Thus

\[
\boxed{
\widetilde\lambda_q\{x:|aqx+c|_q\le u\}
\ll \frac{u}{q}
}
\tag{16}
\]

in the same range.

No prime-pair correlation, Goldbach input, Dirichlet `L`-function estimate, or RH is used in (14)--(16). One source coordinate is conditioned on and the remaining condition is only a union of one-dimensional intervals.

## 2. Logarithmic-depth shelling removes the maximum-atom loss

Let

\[
m:=\lfloor\varepsilon q\rfloor,
\qquad
u_j:=m e^{-j}.
\]

Assume (2). For

\[
0\le j\le J:=\left\lfloor\frac{L}{6}\right\rfloor,
\]

we have uniformly for every `1<=|a|<=B`

\[
\frac{\nu_j}{|a|}
\ge
\frac{m}{B}e^{-J}
\gg q^{1/6}.
\tag{17}
\]

Hence (14) and (16) imply, for either source `mu in {nu_q, widetilde lambda_q}` and every shift `c`,

\[
\mu\{|aX+c|_q\le\nu_j\}
\ll \varepsilon e^{-j}.
\tag{18}
\]

On the depth band

\[
\nu_{j+1}<|aX+c|_q\le\nu_j,
\]

equation (8) gives `|delta|^2<< (j+2)^2`. Therefore

\[
\sum_{j=0}^{J}
(j+2)^2\,
\mu\{|aX+c|_q\le\nu_j\}
\ll
\varepsilon
\sum_{j\ge0}(j+2)^2e^{-j}
\ll\varepsilon.
\tag{19}
\]

The remaining deep tail satisfies

\[
|aX+c|_q\le \nu_J
\ll \varepsilon q^{5/6}.
\tag{20}
\]

Because `q` is prime and `a` is nonzero modulo `q`, multiplication by `a` permutes `Z/qZ`. Thus this tail contains only `O(nu_J+1)` possible source residues. PC-287 gives maximal atom `O(L/q)` for both `nu_q` and `widetilde lambda_q`, so its total mass is

\[
\ll
\varepsilon q^{-1/6}L+\frac{L}{q}.
\tag{21}
\]

The clipping discrepancy is everywhere `O(L)` on that tail, including the exact collision residue. Hence its contribution to the second moment is

\[
\ll
\varepsilon q^{-1/6}L^3+rac{L^3}{q}.
\tag{22}
\]

Since `q^{-1/6}L^3=o(1)`, equations (19)--(22) prove the uniform one-entry estimate

\[
\boxed{
\mathbb E_\mu
|\delta_{q,\varepsilon}(aX+c)|^2
\ll
\varepsilon+\frac{L^3}{q},
}
\tag{23}
\]

for both source laws.

This is the load-bearing improvement over PC-287. Its bound `epsilon L+L^3/q` used only the maximal atom on the whole exceptional arc. Equation (23) uses the arithmetic fact that, down to depth `exp(-L/6)`, the exceptional arc pulls back to long prime intervals and therefore has the correct arc-length mass up to an absolute constant.

## 3. Every noncentral matrix entry inherits the short-interval bound

For a noncentral index `(h,k) in H_B^2`, at least one of `h,k` is nonzero. If `h!=0`, condition on the second source coordinate `y=r/q`; then the phase residue is

\[
hp+kr\pmod q,
\]

so (23) applies with `a=h` and `c=kr`. If `h=0`, use `a=k` after conditioning on the first coordinate. The estimate is therefore uniform over every noncentral entry and under either product source law.

The central `(0,0)` coefficient has zero clipping error because PC-287 keeps its exact source-independent value `-log q`. Summing (23) over the remaining `N^2-1` entries and dividing by the matrix normalization `N^2` gives

\[
\boxed{
\mathbb E
\left\|
\frac{K_{q,B}-\widehat K^{(\varepsilon)}_{q,B}}{N}
\right\|_F^2
\ll
\varepsilon+\frac{L^3}{q}.
}
\tag{24}
\]

Jensen, operator-norm domination by Frobenius norm, and coordinatewise singular-value perturbation then imply that clipping changes each complete normalized ordered singular-spectrum law by

\[
\boxed{
W_1^{(\ell^\infty)}
\ll
\sqrt{\varepsilon+\frac{L^3}{q}}.
}
\tag{25}
\]

This argument does not assume additive pseudorandomness of pairs of primes. In particular it does not replace the one-coordinate conditioning by an unproved claim that the convolution of two prime sources is uniform modulo `q`.

## 4. Combine with the PC-288 path-variation transport

PC-288 proves for the same flat-clipped matrix that every `1`-Lipschitz test of the normalized ordered singular-value vector has one-coordinate path variation

\[
\operatorname{Var}\ll \frac{B}{\sqrt\varepsilon}.
\tag{26}
\]

One-dimensional Stieltjes/Koksma transport in each source coordinate therefore gives

\[
W_1^{(\ell^\infty)}
\left(
\widehat\rho^{prime,(\varepsilon)}_{q,B},
\widehat\rho^{Li,(\varepsilon)}_{q,B}
\right)
\ll
\frac{B}{\sqrt\varepsilon}\Delta_q.
\tag{27}
\]

Add the two clipping errors (25) and the unchanged `O(L^2/q)` distinct-prime-pair correction of PC-287/PC-288. This proves (1).

Under RH, insert (3) into (1):

\[
W_1^{(\ell^\infty)}
\ll
\sqrt{\varepsilon+\frac{L^3}{q}}
+
\frac{Bq^{-1/2}L^2}{\sqrt\varepsilon}
+
\frac{BL}{q\sqrt\varepsilon}
+
\frac{L^2}{q}.
\tag{28}
\]

Balance the first source-dependent clipping term with the leading RH transport term by (4). Then

\[
\sqrt{\varepsilon_q}
=
\frac{Bq^{-1/2}L^2}{\sqrt{\varepsilon_q}}
=
B^{1/2}q^{-1/4}L,
\tag{29}
\]

and

\[
\frac{BL}{q\sqrt{\varepsilon_q}}
=
B^{1/2}q^{-3/4}.
\tag{30}
\]

The inherited exact-collision floor contributes `L^(3/2)/sqrt(q)`. This proves (5). For every sequence

\[
B=o(\sqrt q/L^2),
\]

we have `epsilon_q=o(1)`, `epsilon_q>=1/q`, `2B+1<=q`, and (2) for all sufficiently large `q`, so all hypotheses hold and (6) follows.

## 5. Prior art and novelty audit

The short-interval input is classical sieve theory. Olivier Ramaré and Jan-Christoph Schlage-Puchta, *Improving on the Brun--Titchmarsh theorem*, Acta Arithmetica 131:4 (2008), 351--366, DOI `10.4064/aa131-4-4`, prove the uniform arbitrary-interval estimate used in (11), including the explicit `2H/(log H+3.53)` bound for sufficiently large `H`. The remaining ingredients are already audited in PC-287/PC-288: the log-sine clipping profile, Frobenius/singular-value perturbation, one-dimensional Koksma/Stieltjes transport, and the RH Schoenfeld prime-counting estimate.

Targeted searches against Brun--Titchmarsh short-interval bounds combined with log-sine/cyclotomic finite sections, singular-value laws, and prime-circle matrices found the sieve theorem and neighboring prime-pseudorandomness literature, but no theorem matching (1)--(6). No novelty is claimed for Brun--Titchmarsh, logarithmic depth decomposition, matrix perturbation, Koksma transport, or the RH source bound.

The durable project-local delta is narrower: the PC-287 clipping loss can be re-estimated **after pulling the singular arc back through each exact linear phase map**. In the bandwidth regime relevant to PC-288, those preimages are long enough for classical short-interval sieve density to replace the maximum-atom bound. This moves the exact same one-profile boundary-log observable and exact same Li-grid control from the `log^(5/2)` RH gap to `log^2` without changing the matrix or importing any new zeta-sensitive observable.

No `SOURCES.md` change is needed for the logical dependency: the new external ingredient is a standard one-dimensional prime-interval upper bound, and its full bibliographic anchor and exact role are recorded here.

## 6. Boundaries and falsification

The result is conditional only at the final source-transport step. Equations (14)--(25) are unconditional for the stated geometric regime; RH enters solely through (3). Accordingly (6) is again a one-way consequence of RH, not an RH criterion and not evidence for RH by itself. An order-one prime-versus-Li separation in the range (6), with the exact persisted normalization and control, would contradict RH.

The scale condition (2) is essential to this proof. It ensures that the shallow and medium logarithmic-depth bands pull back to ordinary prime intervals of polynomial length, where (11) removes the maximal-atom loss. The very deepest `exp(-L/6)` tail is deliberately handled by the crude atom bound. The optimized choice (4) lies safely inside this regime, so (2) does not restrict the claimed `log^2` boundary.

The decisive checks are elementary and local: the preimage of a residue arc under `p -> ap+c mod q` must decompose into `O(|a|)` intervals of total length `O(u)`; (11) must be applied only where each interval length is `>=q^(1/6)`; multiplication by nonzero `a mod q` must remain a permutation for the deep-tail cardinality bound; and the Li-grid projection padding must stay `o(u/q)` in the same range. Violating any of these would restore a logarithmic loss and invalidate (1).

The remaining asymptotic gap is now

\[
\boxed{B=o(\sqrt q/(\log q)^2)}
\]

versus the denominator-microscopic scale `B asy sqrt(q)`. This finding does not show that the `log^2` gap is intrinsic. Rather, after the short-interval correction, the visible leading loss is the `q^(-1/2)(log q)^2` Kolmogorov discrepancy supplied by the standard pointwise RH prime-counting bound. Any further one-profile improvement must therefore sharpen how that source discrepancy pairs with the spectral path, exploit additional cancellation not captured by Kolmogorov transport, or prove that the remaining gap marks a genuine finite-section transition. If none of those succeeds, the Mind's alternative remains unchanged: leave the one-profile architecture for a genuinely information-preserving cross-level or multi-source observable.
