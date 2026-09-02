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
2. after defining each local factor at zero by its removable limit
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
   Then `0<C_*<infinity` and the logarithmic derivative of (1) satisfies
   \[
   \boxed{
   \frac{d}{ds}\log\mathcal R_0(s)
   \sim C_*\log\frac1s
   \qquad(s\downarrow0).
   }
   \tag{7}
   \]
   Equivalently,
   \[
   \boxed{
   \log\mathcal R_0(s)-\log\mathcal R_0(0)
   \sim
   C_*\,s\log\frac1s.
   }
   \tag{8}
   \]

Hence the natural connected bottom product has a finite nonzero boundary value but no meromorphic continuation through `s=0` agreeing with its holomorphic right-half-plane germ: a meromorphic continuation with the nonzero finite limit (4) would be holomorphic and nonvanishing at zero, whereas (7) forces its logarithmic derivative to diverge.

The conclusion concerns exactly the selected canonical relative product (1). A separately renormalized object that explicitly subtracts the `s log s` branch is a different object and would require its own intrinsic and spectral justification.

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

The same expression tends to `1` as `s downarrow 0`. Therefore for every `s>=0`, with the zero value interpreted by (3),

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

The BHP gap envelope already used in PF-158 gives a uniform positive logarithmic lower bound for the far-separator length. Indeed PF-158 has

\[
\chi\gg \frac{c^2}{a^\theta Z},
\qquad
Z\ll c^\theta,
\qquad
\theta=0.525,
\tag{14}
\]

and `a<=c/4`, so

\[
\chi\gg c^{2-2\theta}.
\tag{15}
\]

Since `L=4 asinh sqrt(chi)`, while PF-159 changes `L` to `widehat L` only by a bounded left-edge response and (13) changes it to `L^+` by `o(1)` in the far tail, there are absolute constants `kappa>0` and `C_0` such that

\[
\min(L^+,\widehat L)
\ge \kappa\log c-C_0
\tag{16}
\]

throughout the far tail, after harmless finitely many exceptions. Hence

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

The classical prime estimate

\[
\sum_p\frac1{p\log p}<\infty
\tag{18}
\]

now gives

\[
\sum_a\sum_{c\ge4a}
\left|\log\frac{L^+}{\widehat L}\right|<\infty,
\tag{19}
\]

because `sum_a a^-2<infinity` and the `c^-3/log c` term is even absolutely summable over all integers. Equations (12) and (19) prove (2).

By (10), the Weierstrass M-test then gives uniform absolute convergence of the logarithm of (1) for all real `s` in a compact interval containing zero. Every limiting factor is positive, so exponentiating proves (4) and continuity at zero.

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
\tag{20}
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
\tag{21}
\]

It is useful to normalize

\[
\boxed{
h(x):=-2\phi(x)
=2\frac{(x-1)e^x+1}{(e^x-1)^2}.}
\tag{22}
\]

For `x>=0`,

\[
0<h(x)\le1,
\qquad
h(0)=1,
\qquad
h(x)=O((1+x)e^{-x})
\quad(x\to\infty).
\tag{23}
\]

The positivity follows because `((x-1)e^x+1)'=xe^x>=0`; the upper bound is equivalent to `sinh x>=x`.

Now fix one left exterior prime pair `a<b`. PF-160 proves the exact far-right asymptotic

\[
\boxed{
L^+_{a,c}-\widehat L_{a,c}
=-\frac{2A_a}{c}+o(c^{-1}),
\qquad
A_a=e(a)+e(b)>0.
}
\tag{24}
\]

By the mean-value theorem, for some length `xi_{a,c}` between `L^+_{a,c}` and `widehat L_{a,c}`,

\[
q_s(L^+_{a,c})-q_s(\widehat L_{a,c})
=
\left(\frac{A_a}{c}+o(c^{-1})\right)
h(s\xi_{a,c}).
\tag{25}
\]

For fixed `a`, the same BHP estimates used above and the crude upper cross-ratio bound of PF-158 give

\[
\kappa_a\log c-C_a
\le
\xi_{a,c}
\le
K_a\log c+C_a
\tag{26}
\]

for all sufficiently large right primes. Thus the kernel `h(s xi)` is asymptotically `1` while `log c << 1/s`, and is exponentially damped once `log c >> 1/s`.

Mertens' classical theorem for primes,

\[
\sum_{p\le x}\frac1p
=
\log\log x+B+o(1),
\tag{27}
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
\tag{28}
\]

The coefficient does not depend on the precise bounded ratio `xi/log c`: changing the exponential cutoff from `c≈exp(1/(Ks))` to `c≈exp(1/(kappa s))` changes `log log c` only by an additive constant. Equation (23) controls the tail beyond that window. The `o(1/c)` error in (24) is harmless by first fixing its relative size beyond a large right label and then applying the same prime-harmonic cutoff.

This sharpens PF-160's statement `sum_c T_c(0)=+infinity`: the divergence seen by ordinary termwise evaluation is exactly the `s downarrow 0` logarithmic growth of the true right-half-plane logarithmic derivative.

## 3. The fixed-left cusps sum to one finite positive global coefficient

The coefficients in (28) are summable. PF-160 has `e(x)=O(x^-2)`, so

\[
0<C_*:=\sum_a A_a<\infty.
\tag{29}
\]

In fact, because consecutive odd-prime pairs overlap,

\[
C_*=e(3)+2\sum_{p\ge5\atop p\ {m prime}}e(p).
\tag{30}
\]

To justify summing (28) over the left gaps, use the same near/far decomposition as in Section 1. On near spans, the lengths are `O(log a)` and (11) gives a total contribution

\[
O(a^{-2}\log a)
\tag{31}
\]

uniformly for `0<s<=1`. On far spans, (13), the bound `|phi|<=1/2`, the logarithmic lower bound (16), and the exponential decay in (23) give

\[
\sum_{c\ge4a}
\left|q_s(L^+_{a,c})-q_s(\widehat L_{a,c})\right|
\le
C a^{-2}\left(1+\log\frac1s\right)+Ca^{-2}.
\tag{32}
\]

One way to see the logarithm in (32) is to dominate the far prime sum by the classical prime zeta tail `P(1+alpha)=O(1+log(1/alpha))` with `alpha` proportional to `s`. The `c^-3` part of (13) is uniformly summable.

After division by `log(1/s)`, (31)--(32) provide a summable majorant over left primes. Dominated convergence applied to (28) therefore gives

\[
\boxed{
G_0(s)
\sim
C_*\log\frac1s.
}
\tag{33}
\]

This proves (7).

## 4. The product has an `s log s` cusp, not a zero or pole

PF-160 proves that `G_0` is holomorphic on `Re s>0` as the difference

\[
G_0(s)=G_{\rm conn}(s)-G_{\rm conn}(s+1).
\tag{34}
\]

Choose any positive real anchor `s_0`. The holomorphic germ determined by integrating `G_0` and normalizing to the convergent direct product (1) at `s_0` agrees with (1) on the positive real axis. Section 1 gives its finite nonzero boundary value at zero.

Equation (33) is integrable at zero, and

\[
\int_0^s\log\frac1t\,dt
=
s\log\frac1s+s.
\tag{35}
\]

Taking the limit from a positive lower endpoint therefore yields

\[
\log\mathcal R_0(s)-\log\mathcal R_0(0)
=
\int_0^sG_0(t)\,dt
\sim
C_*s\log\frac1s,
\tag{36}
\]

which proves (8).

This separates three notions that PF-160 deliberately left open:

- the **termwise logarithmic derivative** does diverge at zero;
- the **underlying direct product** nevertheless converges to a finite nonzero number;
- the right-half-plane germ is **not meromorphic through zero**, because its derivative has the logarithmic divergence (33), not an integer-order Laurent behavior.

So `s=0` is a branch-type cusp of this selected relative product, not a spectral zero or pole.

## 5. Adversarial checks

**Could the PF-160 divergence secretly mean that the product vanishes?** No. Equation (2) is stronger than conditional convergence: the zero-boundary logarithms are absolutely summable, so (4) is finite and strictly positive.

**Could infinitely many very long separators destroy the zero-boundary product?** No. Their matched length defect gains the `1/c` factor in PF-159, while the separator length itself is at least logarithmic in `c`. The resulting `1/(c log c)` prime sum converges.

**Could the cusp coefficient cancel after summing over left gaps?** No. Every fixed-left coefficient `A_a=e(a)+e(b)` is strictly positive, and their sum is finite. The uniform estimate (32) permits the fixed-left asymptotics to be summed.

**Is the logarithmic divergence an uncancelled local `1/s` pole?** No. PF-160 already proves that the `1/s` term cancels inside every matched local factor. Equations (22)--(25) show that the global divergence comes from an increasing number of far-right factors with `sL=O(1)`, each carrying a reciprocal-prime defect.

**Does failure of meromorphic continuation here imply failure for the full surface Ruelle/Selberg object?** No. The prime flute has no ordinary full Selberg/Ruelle Euler product in the standard sense by PF-035/PF-036/PF-075/PF-077. The present object is only the explicitly selected and exactly matched PF-004 canonical-separator bottom sector.

**Could a regularization cross zero?** Possibly, but it would have to remove the explicit `C_* s log s` branch. That would define a different renormalized object; no claim of impossibility is made for such a construction. The point is that the natural direct product itself has no zero/pole and no hidden meromorphic divisor at the boundary.

**Is the cusp an RH signal?** No. The critical line `Re s=1/2` lies inside the zero-free positive half-plane already isolated by PF-159/PF-160. The new boundary behavior occurs at zero and is generated by the classical reciprocal-prime logarithm after exact prime/all-composite-shift matching.

## 6. Prior-art and novelty audit

The analytic ingredients are classical. Mertens' prime theorem (27), convergence of `sum_p 1/(p log p)`, and the prime-zeta asymptotic

\[
P(1+t)=\log(1/t)+O(1)
\]

are standard analytic number theory. A classical reference for the prime-zeta framework is C.-E. Fröberg, *On the prime zeta function*, BIT 8 (1968), 187--202. No novelty is claimed for these facts or for the elementary infinite-product criterion used in Section 1.

The identity between the bottom Selberg factor and a Ruelle factor is also classical. In finite/cofinite hyperbolic settings the resulting Ruelle zeta is meromorphic and its order at zero is controlled by topological/scattering data; for example Lee-Peng Teo, *Ruelle zeta function for cofinite hyperbolic Riemann surfaces with ramification points*, Letters in Mathematical Physics 110 (2020), 61--82, DOI `10.1007/s11005-019-01222-7`, studies precisely such integer-order zero/pole behavior. Those theorems do not apply to this infinitely generated zero-systole flute or to the selected relative canonical-separator product (1).

Directed searches for Ruelle/Selberg theory on infinite-type or flute surfaces did not locate a theorem covering the exact PF-159 one-ended subtraction, the project-specific asymptotic (24), or the resulting boundary product (4)/(8). The durable Mathia content is therefore not a claim of a new general Ruelle theorem but the exact specialization

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
\tag{37}
\]

## 7. Consequence for the prime-flute program

PF-158 found a sharp `1/4` ordinary boundary for the unrenormalized canonical Selberg cocycle. PF-159 showed that boundary was a one-ended propagation artifact and pushed the connected object to `Re s>0`. PF-160 then showed that the remaining zero boundary is entirely the bottom Ruelle layer and has a harmonic-prime termwise divergence.

PF-161 closes the natural remaining interpretation of that boundary: **the bottom connected product does not acquire a zero or pole at zero.** Its value stays finite and nonzero, while the derivative develops a classical logarithmic cusp. Therefore neither the `1/4` boundary nor the residual `0` boundary supplies a critical-line divisor or an RH selector in the complete canonical-separator sector.

Any surviving zeta-relevant prime-flute mechanism must therefore use spectral/dynamical information outside this selected canonical separator product, rather than extracting significance from its ordinary-convergence boundaries.