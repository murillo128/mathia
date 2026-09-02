# PF-161 — connected bottom Ruelle product has a nonzero logarithmic cusp at zero

**Status:** `EXACT-DERIVED + CLASSICAL-INPUT + LITERATURE-AUDITED + DECISIVE-NEGATIVE/BOUNDARY`. PF-160 proves that the ordinary connected canonical-separator logarithmic derivative has a sharp boundary at `s=0`, carried entirely by the bottom Selberg/Ruelle layer: for each fixed left exterior prime gap its termwise finite parts have a positive reciprocal-prime tail. The present finding identifies what that divergence means for the underlying natural relative bottom product. The product itself converges at `s=0` to a finite strictly positive value; it has neither a zero nor a pole there. Instead its logarithmic derivative grows like `C_* log(1/s)`, so the product has a non-meromorphic `s log(1/s)` cusp.

Thus the last ordinary-convergence obstruction left by PF-159/PF-160 is not a hidden spectral divisor. It is a classical prime-harmonic branch effect in a selected relative Ruelle-type sector. This is not a full Ruelle zeta function for the infinite flute, does not construct a spectral determinant, and has no RH implication.

## Claim

Use the notation of PF-159--PF-160. For every canonical PF-004 separator `eta` with consecutive exterior prime pairs

\[
a<b<c<d,
\]

let `L_eta^+` be its length on the exact all-composite shift clone, and let `\widehat L_eta` be PF-159's exact one-ended comparison length

\[
\widehat\chi_{a,c}=R_a\chi_{a,c},
\qquad
R_a=\frac{X}{X^+}>1,
\qquad
\widehat L_{a,c}=4\operatorname{arsinh}\sqrt{\widehat\chi_{a,c}}.
\]

For real `s>0`, define the connected canonical **bottom Ruelle product**

\[
\boxed{
\mathcal R_0(s)
:=
\prod_{\eta\in\mathcal C}
\frac{1-e^{-sL_\eta^+}}
     {1-e^{-s\widehat L_\eta}}.
}
\tag{1}
\]

This is the `m=0` quotient selected by PF-160 from the connected Selberg cocycle; it is not the full surface Ruelle zeta function.

Then:

1. the zero-boundary length-ratio series is absolutely convergent,
   \[
   \boxed{
   \sum_{\eta\in\mathcal C}
   \left|\log\frac{L_\eta^+}{\widehat L_\eta}\right|<\infty;
   }
   \tag{2}
   \]
2. after defining each local factor at zero by
   \[
   \frac{1-e^{-sL^+}}{1-e^{-s\widehat L}}
   \longrightarrow
   \frac{L^+}{\widehat L},
   \qquad s\downarrow0,
   \tag{3}
   \]
   the product in (1) converges uniformly and absolutely in logarithm on every real compact interval `0<=s<=S`;
3. consequently
   \[
   \boxed{
   0<\mathcal R_0(0)
   :=
   \prod_{\eta\in\mathcal C}
   \frac{L_\eta^+}{\widehat L_\eta}
   <\infty,
   }
   \tag{4}
   \]
   and `mathcal R_0(s) -> mathcal R_0(0)` as `s downarrow 0`;
4. writing
   \[
   e(x):=\pi\cot\frac{\pi}{x+1}-\pi\cot\frac{\pi}{x}-1,
   \tag{5}
   \]
   so that PF-160 has `e(x)>0` and `e(x)=O(x^-2)`, and denoting by `b` the prime immediately after a left prime `a`, put
   \[
   A_a:=e(a)+e(b)>0,
   \qquad
   C_*:=\sum_a A_a.
   \tag{6}
   \]
   Then `0<C_*<infinity` and
   \[
   \boxed{
   \frac{d}{ds}\log\mathcal R_0(s)
   \sim C_*\log\frac1s
   \qquad(s\downarrow0),
   }
   \tag{7}
   \]
   equivalently
   \[
   \boxed{
   \log\mathcal R_0(s)-\log\mathcal R_0(0)
   \sim
   C_*s\log\frac1s.
   }
   \tag{8}
   \]

Hence the natural connected bottom product has a finite nonzero boundary value but no meromorphic continuation through `s=0` agreeing with its holomorphic right-half-plane germ: a meromorphic continuation with the nonzero finite limit (4) would be holomorphic and nonvanishing at zero, whereas (7) forces its logarithmic derivative to diverge.

The conclusion concerns exactly the selected canonical relative product (1). A separately renormalized object that explicitly removes the `s log s` branch is a different object and would require its own intrinsic and spectral justification.

## 1. The zero-boundary product is absolutely convergent

For `s>0` and `L>0`, set

\[
f_s(L):=\log(1-e^{-sL}).
\]

In the logarithmic length coordinate,

\[
\boxed{
\frac{\partial f_s}{\partial\log L}
=
\frac{sL}{e^{sL}-1}
\in(0,1].
}
\tag{9}
\]

The same expression tends to `1` as `s downarrow 0`. Therefore for every real `s>=0`, with the zero value interpreted by (3),

\[
\boxed{
\left|
\log\frac{1-e^{-sL^+}}{1-e^{-s\widehat L}}
\right|
\le
\left|\log\frac{L^+}{\widehat L}\right|.
}
\tag{10}
\]

It remains to sum the right-hand side over all canonical separators.

For the **near-span** sector `c<4a`, PF-159 gives

\[
\left|\log\frac{L^+}{\widehat L}\right|=O(a^{-3}).
\tag{11}
\]

There are at most `O(a)` possible right integer labels `c<4a`, hence certainly at most `O(a)` right prime gaps. Thus

\[
\sum_a\sum_{c<4a}
\left|\log\frac{L^+}{\widehat L}\right|
\ll
\sum_a a^{-2}<\infty.
\tag{12}
\]

For the **far-span** sector `c>=4a`, PF-159 proves

\[
|L^+-\widehat L|
\le
C\left(\frac{a^{-2}}c+c^{-3}\right).
\tag{13}
\]

The BHP gap envelope already used in PF-158 gives a uniform positive logarithmic lower bound for the far-separator length. PF-158 has

\[
\chi\gg \frac{c^2}{a^\theta Z},
\qquad
Z\ll c^\theta,
\qquad
\theta=0.525.
\tag{14}
\]

Since `a<=c/4`,

\[
\chi\gg c^{2-2\theta}.
\tag{15}
\]

Because `L=4 asinh sqrt(chi)`, while PF-159 changes `L` to `widehat L` only by a bounded left-edge response and (13) changes it to `L^+` by `o(1)` in the far tail, there are absolute constants `kappa>0` and `C_0` such that

\[
\min(L^+,\widehat L)
\ge \kappa\log c-C_0
\tag{16}
\]

throughout the far tail, apart from finitely many harmless pairs. Hence

\[
\left|\log\frac{L^+}{\widehat L}\right|
\le
\frac{|L^+-\widehat L|}{\min(L^+,\widehat L)}
\ll
\frac{a^{-2}}{c\log c}
+
\frac{c^{-3}}{\log c}.
\tag{17}
\]

The classical estimate

\[
\sum_p\frac1{p\log p}<\infty
\tag{18}
\]

handles the first term after summing in `c`, because its complete `c`-sum is finite and `sum_a a^-2<infinity`. For the second term one must retain the multiplicity in the left label: for each right prime `c`, there are at most `c` possible integers `a<c/4`, so

\[
\sum_c\sum_{a\le c/4}
\frac{c^{-3}}{\log c}
\ll
\sum_{c\ge3}\frac1{c^2\log c}<\infty.
\tag{19}
\]

Thus

\[
\boxed{
\sum_{\eta\in\mathcal C}
\left|\log\frac{L_\eta^+}{\widehat L_\eta}\right|<\infty.
}
\tag{20}
\]

By (10), the Weierstrass M-test gives uniform absolute convergence of the logarithm of (1) on every real compact interval containing zero. Every limiting factor is positive, so exponentiating proves (4) and continuity at zero.

One convenient classical route to (18) is the prime-zeta identity: `P(1+t)=sum_p p^(-1-t)` has the standard logarithmic singularity `P(1+t)=log(1/t)+O(1)`, and integrating in `t` gives `sum_p 1/(p log p)<infinity`. No prime-flute input enters that number-theoretic step.

## 2. PF-160's harmonic tail becomes a logarithmic derivative cusp

The logarithmic derivative of one local bottom factor is

\[
q_s(L):=\frac{L}{e^{sL}-1},
\]

so PF-160's function is exactly

\[
G_0(s)
=
\frac{d}{ds}\log\mathcal R_0(s)
=
\sum_{\eta\in\mathcal C}
\left[q_s(L_\eta^+)-q_s(\widehat L_\eta)\right],
\qquad s>0.
\tag{21}
\]

Differentiate with respect to length. If `x=sL`,

\[
\frac{\partial q_s}{\partial L}
=
\phi(x),
\qquad
\phi(x)
=
\frac{e^x-1-xe^x}{(e^x-1)^2}.
\tag{22}
\]

Normalize

\[
\boxed{
h(x):=-2\phi(x)
=2\frac{(x-1)e^x+1}{(e^x-1)^2}.}
\tag{23}
\]

For `x>=0`,

\[
0<h(x)\le1,
\qquad
h(0)=1,
\qquad
h(x)=O((1+x)e^{-x})
\quad(x\to\infty).
\tag{24}
\]

The positivity follows because `((x-1)e^x+1)'=xe^x>=0`; the upper bound is equivalent to `sinh x>=x`.

Fix one left exterior prime pair `a<b`. PF-160 proves the exact far-right asymptotic

\[
\boxed{
L^+_{a,c}-\widehat L_{a,c}
=-\frac{2A_a}{c}+o(c^{-1}),
\qquad
A_a=e(a)+e(b)>0.
}
\tag{25}
\]

By the mean-value theorem, for some length `xi_{a,c}` between `L^+_{a,c}` and `widehat L_{a,c}`,

\[
q_s(L^+_{a,c})-q_s(\widehat L_{a,c})
=
\left(\frac{A_a}{c}+o(c^{-1})\right)
h(s\xi_{a,c}).
\tag{26}
\]

For fixed `a`, the same lower estimate as above and PF-158's crude upper cross-ratio bound give

\[
\kappa_a\log c-C_a
\le
\xi_{a,c}
\le
K_a\log c+C_a
\tag{27}
\]

for all sufficiently large right primes. Thus `h(s xi)` is close to `1` while `log c << 1/s` and exponentially damped once `log c >> 1/s`.

Mertens' classical theorem for primes,

\[
\sum_{p\le x}\frac1p
=
\log\log x+B+o(1),
\tag{28}
\]

then gives the Abelian cutoff law

\[
\boxed{
\sum_c
\left[q_s(L^+_{a,c})-q_s(\widehat L_{a,c})\right]
\sim
A_a\log\frac1s
\qquad(s\downarrow0).
}
\tag{29}
\]

For completeness, the coefficient does not depend on the precise bounded ratio `xi/log c`. For a small fixed `epsilon>0`, all primes with `c<=exp(epsilon/s)` have `h(s xi)=1+O(epsilon)` and already contribute `(1+O(epsilon))log(1/s)+O(1)` by (28). For an upper bound, `h<=1` handles primes up to `exp(M/s)`, while the exponential estimate in (24), together with a standard Chebyshev/Mertens prime-counting bound, makes the tail beyond `exp(M/s)` only `O_M(1)`. Letting `epsilon downarrow0` and then `M to infinity` gives coefficient `1`. The `o(1/c)` error in (25) is treated by first fixing its relative size beyond a large right label and applying the same cutoff.

This sharpens PF-160's statement `sum_c T_c(0)=+infinity`: the divergence seen by ordinary termwise evaluation is exactly the `s downarrow 0` logarithmic growth of the genuine right-half-plane logarithmic derivative.

## 3. The fixed-left cusps sum to one finite positive global coefficient

The coefficients in (29) are summable. PF-160 has `e(x)=O(x^-2)`, so

\[
0<C_*:=\sum_a A_a<\infty.
\tag{30}
\]

Because consecutive odd-prime pairs overlap,

\[
C_*=e(3)+2\sum_{p\ge5\atop p\ {m prime}}e(p).
\tag{31}
\]

To justify summing (29) over the left gaps, use the same near/far decomposition. On near spans, the cross-ratio is at most polynomial in `a`, hence both matched lengths are `O(log a)`; together with (11) and the boundedness of `phi`, the total near-span contribution for one left `a` is

\[
O(a^{-2}\log a)
\tag{32}
\]

uniformly for `0<s<=1`.

On far spans, (13), (16), and the exponential part of (24) give, for `0<s<=1/2`,

\[
\sum_{c\ge4a}
\left|q_s(L^+_{a,c})-q_s(\widehat L_{a,c})\right|
\le
C a^{-2}\left(1+\log\frac1s\right)+Ca^{-2}.
\tag{33}
\]

Indeed the `a^-2/c` part is dominated by a prime-zeta tail `P(1+alpha)=O(1+log(1/alpha))` with `alpha` proportional to `s`, while the `c^-3` part sums to `O(a^-2)` even over all integers `c>=4a`.

After division by `log(1/s)`, (32)--(33) give the summable left-label majorant

\[
C a^{-2}(1+\log a).
\tag{34}
\]

Dominated convergence applied to (29) therefore yields

\[
\boxed{
G_0(s)
\sim
C_*\log\frac1s.
}
\tag{35}
\]

This proves (7).

## 4. The product has an `s log s` cusp, not a zero or pole

PF-160 proves that `G_0` is holomorphic on `Re s>0` as

\[
G_0(s)=G_{\rm conn}(s)-G_{\rm conn}(s+1).
\tag{36}
\]

Choose any positive real anchor `s_0`. Integrating `G_0` and normalizing to the convergent direct product (1) at `s_0` defines its holomorphic right-half-plane germ. On the positive real axis this germ agrees with the direct product, whose finite nonzero limit was proved in Section 1.

Equation (35) is integrable at zero, and

\[
\int_0^s\log\frac1t\,dt
=
s\log\frac1s+s.
\tag{37}
\]

Taking the lower endpoint to zero therefore gives

\[
\log\mathcal R_0(s)-\log\mathcal R_0(0)
=
\int_0^sG_0(t)\,dt
\sim
C_*s\log\frac1s,
\tag{38}
\]

which proves (8).

This separates three notions that PF-160 deliberately left open:

- the **termwise logarithmic derivative** does diverge at zero;
- the **underlying direct product** nevertheless converges to a finite nonzero number;
- the right-half-plane germ is **not meromorphic through zero**, because its logarithmic derivative has the divergence (35), not finite Taylor/Laurent behavior compatible with a nonzero finite boundary value.

So `s=0` is a branch-type cusp of this selected relative product, not a spectral zero or pole.

## 5. Adversarial checks

**Could the PF-160 divergence secretly mean that the product vanishes?** No. Equation (20) is stronger than conditional convergence: the zero-boundary logarithms are absolutely summable, so (4) is finite and strictly positive.

**Could infinitely many very long separators destroy the zero-boundary product?** No. Their matched length defect gains the `1/c` factor in PF-159, while the separator length itself is at least logarithmic in `c`. The resulting leading `1/(c log c)` prime sum converges; the two-label multiplicity in the `c^-3` remainder is explicitly controlled in (19).

**Could the cusp coefficient cancel after summing over left gaps?** No. Every fixed-left coefficient `A_a=e(a)+e(b)` is strictly positive, their sum is finite, and (34) permits the fixed-left asymptotics to be summed.

**Is the logarithmic divergence an uncancelled local `1/s` pole?** No. PF-160 already proves that the `1/s` term cancels inside every matched local factor. Equations (23)--(26) show that the global divergence comes from an increasing number of far-right factors with `sL=O(1)`, each carrying a reciprocal-prime defect.

**Does failure of meromorphic continuation here imply failure for a full surface Ruelle/Selberg object?** No. The prime flute has no ordinary full Selberg/Ruelle Euler product in the standard sense by PF-035/PF-036/PF-075/PF-077. The present object is only the explicitly selected and exactly matched PF-004 canonical-separator bottom sector.

**Could a regularization cross zero?** Possibly, but it would have to remove the explicit `C_*s log s` branch. That defines a different renormalized object; no impossibility claim is made for such a construction. The point is that the natural direct product itself has no zero/pole and no hidden meromorphic divisor at the boundary.

**Is the cusp an RH signal?** No. The critical line `Re s=1/2` lies inside the zero-free positive half-plane already isolated by PF-159/PF-160. The new boundary behavior occurs at zero and is generated by the classical reciprocal-prime logarithm after exact prime/all-composite-shift matching.

## 6. Prior-art and novelty audit

The analytic ingredients are classical. Mertens' prime theorem (28), convergence of `sum_p 1/(p log p)`, and the prime-zeta asymptotic

\[
P(1+t)=\log(1/t)+O(1)
\]

are standard analytic number theory. A classical reference for the prime-zeta framework is C.-E. Fröberg, *On the prime zeta function*, BIT 8 (1968), 187--202. No novelty is claimed for these facts or for the elementary infinite-product criterion used in Section 1.

The identity between the bottom Selberg factor and a Ruelle factor is also classical. In finite/cofinite hyperbolic settings the resulting Ruelle zeta is meromorphic and its order at zero is controlled by topological/scattering data; for example Lee-Peng Teo, *Ruelle zeta function for cofinite hyperbolic Riemann surfaces with ramification points*, Letters in Mathematical Physics 110 (2020), 61--82, DOI `10.1007/s11005-019-01222-7`, studies such integer-order zero/pole behavior. Those theorems do not apply to this infinitely generated zero-systole flute or to the selected relative canonical-separator product (1).

Directed searches for Ruelle/Selberg theory on infinite-type or flute surfaces did not locate a theorem covering the exact PF-159 one-ended subtraction, the project-specific asymptotic (25), or the resulting boundary product (4)/(8). The durable Mathia content is not a claim of a new general Ruelle theorem but the exact specialization

\[
\boxed{
\text{PF-159 connected length defect}
\to
\sum|\log(L^+/\widehat L)|<\infty
\to
\mathcal R_0(0)\ne0
\to
G_0(s)\sim C_*\log(1/s)
\to
s\log s\text{ cusp rather than a divisor}.}
\tag{39}
\]

## 7. Consequence for the prime-flute program

PF-158 found a sharp `1/4` ordinary boundary for the unrenormalized canonical Selberg cocycle. PF-159 showed that boundary was a one-ended propagation artifact and pushed the connected object to `Re s>0`. PF-160 then showed that the remaining zero boundary is entirely the bottom Ruelle layer and has a harmonic-prime termwise divergence.

PF-161 closes the natural remaining interpretation of that boundary: **the bottom connected product does not acquire a zero or pole at zero.** Its value stays finite and nonzero, while the derivative develops a classical logarithmic cusp. Therefore neither the `1/4` boundary nor the residual `0` boundary supplies a critical-line divisor or an RH selector in the complete canonical-separator sector.

Any surviving zeta-relevant prime-flute mechanism must therefore use spectral/dynamical information outside this selected canonical separator product, rather than extracting significance from its ordinary-convergence boundaries.
