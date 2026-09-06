# ANF-063 — endpoint anti-concentration closes every Montgomery--Taylor moment order from nine onward

**Status:** `EXACT-DERIVED + GLOBAL-FOURIER-ANTI-CONCENTRATION + ALL-FREQUENCY-MOMENT-BOUND + FINITE-ORDER-REDUCTION + STRUCTURAL-STRENGTHENING`. `ANF-062` proves the fixed Montgomery--Taylor five-point defect is positive but leaves open the stronger all-height coercivity mechanism proposed in `CLUE-even-moment-radial-coercivity`. That clue asks whether, for

\[
M_n(t):=\int_{-1}^{1}\alpha^{2n}J_{\rm MT}(\alpha)
\cos(2\pi\alpha t)\,d\alpha,
\qquad n\ge2,
\tag{1}
\]

one has

\[
\boxed{
\frac{M_n(t)}{M_n(0)}
\ge
-\frac{2^{2n-1}}{1+2^{2n-1}}
\qquad(t\in\mathbb R).
}
\tag{2}
\]

The large-order part of that question can be closed analytically and globally in the horizontal frequency. The exact Montgomery--Taylor density has two-sided linear endpoint control. After normalizing `x^(2n) J_MT(x)` to a probability density, a fixed `1/n` endpoint shell therefore carries density of order `n`. No cosine can remain arbitrarily close to `-1` across that shell: an elementary phase-independent `cos^2` integral gives a polynomial gap from `-1`, whereas the right side of (2) approaches `-1` exponentially.

The result is

\[
\boxed{
\frac{M_n(t)}{M_n(0)}
>
-\frac{2^{2n-1}}{1+2^{2n-1}}
\qquad
\text{for every }n\ge9\text{ and every }t\in\mathbb R.
}
\tag{3}
\]

Thus the accepted all-moment clue is no longer an infinite-order problem. **Only the seven orders**

\[
\boxed{n=2,3,4,5,6,7,8}
\tag{4}
\]

remain to be decided. This does not yet prove the sharp five-point coercivity theorem, because any one of those finite orders could still violate the sufficient moment condition.

## 1. Exact endpoint comparison for the Montgomery--Taylor spectrum

On `0<=x<=1`, `ANF-062` records the exact even density

\[
J_{\rm MT}(x)
=
\frac{(1-x)\cos(\sqrt2 x)
      +\sin(\sqrt2(1-x))/\sqrt2}
     {4\sin^2(1/\sqrt2)}.
\tag{5}
\]

Since `0<=sqrt(2)x<=sqrt(2)<pi/2`, cosine is positive and decreasing on the relevant interval. Also `sin u>=0` there and `sin u<=u` for `u>=0`. Hence, with

\[
c_0:=\frac{\cos\sqrt2}{4\sin^2(1/\sqrt2)},
\qquad
C_0:=\frac{1}{2\sin^2(1/\sqrt2)},
\tag{6}
\]

one has the global two-sided comparison

\[
\boxed{
c_0(1-x)\le J_{\rm MT}(x)\le C_0(1-x),
\qquad 0\le x\le1,
}
\tag{7}
\]

and therefore

\[
\boxed{\frac{c_0}{C_0}=\frac{\cos\sqrt2}{2}.}
\tag{8}
\]

This is stronger than merely knowing that the density vanishes linearly at the endpoint: the constants are valid on the whole positive half-support.

Put

\[
D_n:=\int_0^1x^{2n}J_{\rm MT}(x)\,dx.
\tag{9}
\]

Equation (7) and the beta integral give

\[
D_n
\le
\frac{C_0}{(2n+1)(2n+2)}.
\tag{10}
\]

Define the probability density

\[
p_n(x):=\frac{x^{2n}J_{\rm MT}(x)}{D_n},
\qquad 0\le x\le1.
\tag{11}
\]

Evenness of `J_MT` then gives the exact probabilistic form

\[
R_n(t):=\frac{M_n(t)}{M_n(0)}
=\int_0^1p_n(x)\cos(2\pi tx)\,dx.
\tag{12}
\]

## 2. A fixed endpoint shell forces a uniform gap from `-1`

For `n>=2`, take the shell

\[
I_n=
\left[1-\frac{8}{5n},\;1-\frac{2}{5n}\right],
\qquad
|I_n|=\frac{6}{5n}.
\tag{13}
\]

For `x in I_n`, equations (7), (10) and (11) imply

\[
\begin{aligned}
p_n(x)
&\ge
\left(1-\frac{8}{5n}\right)^{2n}
\frac{c_0(2/5n)}{C_0}
(2n+1)(2n+2)\\
&=
\boxed{
\frac{\cos\sqrt2}{5n}
(2n+1)(2n+2)
\left(1-\frac{8}{5n}\right)^{2n}.
}
\end{aligned}
\tag{14}
\]

For any interval `I` of length `L` and any nonzero real `t`, direct integration gives

\[
\int_I\cos^2(\pi tx)\,dx
\ge
\frac L2\left(1-
\frac{|\sin(\pi |t|L)|}{\pi |t|L}
\right).
\tag{15}
\]

The elementary inequality

\[
\boxed{
1-\frac{|\sin z|}{z}
\ge\frac{19}{120}\min(z^2,1),
\qquad z>0,
}
\tag{16}
\]

is enough here. For `0<z<=1`, the alternating Taylor bound

\[
\frac{\sin z}{z}
\le1-\frac{z^2}{6}+\frac{z^4}{120}
\le1-\frac{19}{120}z^2
\tag{17}
\]

proves it. For `z>=1`, `sin z/z` is decreasing on `[1,7/6]`, while

\[
\sin1<1-\frac16+\frac1{120}=\frac{101}{120}<\frac{101}{120}<1-\frac{19}{120},
\tag{18}
\]

and for `z>=7/6` one simply uses `|sin z|/z<=1/z<=6/7<101/120`. Thus (16) holds globally. (The duplicated `101/120` comparison in (18) is deliberately only a rational safety bound; no numerical evaluation of `sin 1` is needed.)

If `|t|<=1/4`, then `cos(2 pi t x)>=0` throughout `[0,1]`, so `R_n(t)>=0` and (2) is automatic. Assume from now on `|t|>=1/4`. With `L=6/(5n)`, put

\[
z=\pi|t|L.
\tag{19}
\]

Since `3pi/(10n)<1`, equation (16) gives

\[
\min(z^2,1)
\ge
\frac{9\pi^2}{100n^2}.
\tag{20}
\]

Substituting (20) into (15) yields the all-frequency shell bound

\[
\boxed{
\int_{I_n}\cos^2(\pi tx)\,dx
\ge
\frac{171\pi^2}{20000n^3}
\qquad(|t|\ge1/4).
}
\tag{21}
\]

Finally, from `1+cos(2u)=2cos^2 u`, equations (12), (14), and (21) give

\[
\boxed{
1+R_n(t)
\ge L_n
:=
\frac{171\pi^2\cos\sqrt2}{50000}
\frac{(2n+1)(2n+2)}{n^4}
\left(1-\frac{8}{5n}\right)^{2n}
}
\tag{22}
\]

for every `n>=2` and every `|t|>=1/4`. Together with the trivial small-frequency positivity, (22) is a global quantitative anti-concentration inequality for every frequency.

## 3. The polynomial gap beats the exponential threshold from `n=9`

The target in (2) can be written

\[
-\frac{2^{2n-1}}{1+2^{2n-1}}
=
-1+\delta_n,
\qquad
\delta_n:=\frac1{1+2^{2n-1}}
<\frac{2}{4^n}.
\tag{23}
\]

No floating-point constants are needed to compare (22) and (23). The classical rational estimates

\[
\pi^2>9,
\qquad
\cos\sqrt2>
1-1+\frac{4}{24}-\frac{8}{720}
=\frac7{45}>\frac3{20}
\tag{24}
\]

imply

\[
L_n>
\frac{4617}{10^6}
\frac{(2n+1)(2n+2)}{n^4}
\left(1-\frac{8}{5n}\right)^{2n}.
\tag{25}
\]

At `n=9`, this rational lower bound satisfies

\[
\frac{4617}{10^6}
\frac{380}{6561}
\left(\frac{37}{45}\right)^{18}
>
\frac1{131072}
=
\frac{2}{4^9}.
\tag{26}
\]

Equation (26) is a direct integer comparison after clearing denominators.

It remains only to show that the comparison gets easier with increasing `n`. The factor

\[
a_n:=\left(1-\frac{8}{5n}\right)^{2n}
\tag{27}
\]

is increasing: for real `x>8/5`, differentiating `2x log(1-8/(5x))` reduces its sign to

\[
\log(1-z)+\frac{z}{1-z}>0,
\qquad 0<z<1,
\tag{28}
\]

whose derivative in `z` is `z/(1-z)^2>0` and whose value at zero is zero. Moreover

\[
4\left(\frac{n}{n+1}\right)^4>1
\qquad(n\ge4),
\tag{29}
\]

so

\[
4^n\frac{(2n+1)(2n+2)}{n^4}
\tag{30}
\]

is strictly increasing for `n>=4` (the omitted ratio of the two consecutive numerator factors is itself greater than one). Therefore `4^n L_n` is increasing for every `n>=9`. Combining (26) with (23) proves

\[
L_n>\frac{2}{4^n}>\delta_n
\qquad(n\ge9).
\tag{31}
\]

Equations (22), (23), and (31), together with the `|t|<=1/4` case, prove (3).

## 4. What this does and does not close

The accepted moment route in `CLUE-even-moment-radial-coercivity` had an infinite quantifier over both moment order and horizontal frequency. Equation (3) removes the first source of noncompactness **without introducing any frequency cutoff**: every real `t` is already controlled for every `n>=9`. The only unresolved moment orders are exactly (4).

This is stronger than the finite numerical checks that motivated the clue. In particular, no large-`n` counterexample can escape by moving its minimizing frequency to infinity. The reason is robust and elementary: the normalized weight has an endpoint shell of width `asymp 1/n` and mass density `asymp n`, while any cosine phase that is near `-1` at one point pays a squared-distance cost across that shell. The resulting `Omega(n^-2)` gap dominates the exponentially small `delta_n` required by (2).

The argument is profile-specific through the exact endpoint comparison (7). It does **not** prove (2) for `n=2,...,8`; it does not prove the sharp coercivity inequality or radial monotonicity until those seven orders are also settled; and it does not address larger conjugation-invariant multisets. A failure at one residual finite order would kill this sufficient all-moment route without contradicting the already certified five-point zero-freeness of `ANF-062`.

## 5. Prior art and audit boundary

The proof uses standard elementary ingredients: endpoint comparison, beta normalization, the identity `1+cos(2u)=2cos^2 u`, a one-interval Fourier anti-concentration estimate, and rational Taylor bounds. Endpoint/Laplace concentration and positive-definite bandlimited extremal methods are classical, and no novelty is claimed for those tools. A targeted check of the Montgomery--Taylor/extremal-function literature and standard endpoint-asymptotic literature did not supply the specific all-order inequality (2) or the finite-order cutoff (3). No external theorem is load-bearing in the derivation, so `SOURCES.md` needs no new anchor.

The decisive audit is finite and exact. Recheck (5), the two-sided endpoint comparison (7), the interval identity (15), the global scalar inequality (16), and the rational comparison (26). If all survive, any refutation of the accepted all-moment route must occur at one of the seven orders in (4); searching larger moment order is mathematically redundant for that question.