# AF-422 — Square-transition detuning controls adjacent-packet cancellation

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `DOUBLE-SCALING` · `SQUARE-TRANSITION` · `SIGNED-RESUMMATION` · `NO-NOVELTY-CLAIM`

## Claim

Continue AF-421 at one of its discrete finite-window saddle transitions. Fix an integer `m>=1`, let

\[
s_n=2n+d_n,\qquad d_n=o(n),
\]

and retain the AF-420/AF-421 effective coordinate

\[
b_n=a\,n^{d_n/n}\longrightarrow m^2,
\qquad a>0.
\]

AF-421 isolates the exact ratio between the two adjacent full-column rectangle amplitudes,

\[
F_{n,m}
=
\left(\frac{a}{n^2}\right)^n
\left(\frac{n+m}{m}\right)^{s_n-1}
\frac{\zeta(2(n+m))}{\zeta(2m)}
\left(\frac{2(n+m)-1}{2m-1}\right)^2.
\tag{1}
\]

Define the next detuning coordinate

\[
\boxed{
\Xi_{n,m}
:=
\log n
+n\log\!\left(\frac{b_n}{m^2}\right)
-d_n\log m
}
\tag{2}
\]

and the positive constant

\[
\boxed{
K_m
:=
\frac{4m e^{2m}}
{(2m-1)^2\zeta(2m)}.
}
\tag{3}
\]

Then

\[
\boxed{
F_{n,m}
=
K_m e^{\Xi_{n,m}}(1+o(1)).
}
\tag{4}
\]

Equivalently,

\[
\log F_{n,m}=\Xi_{n,m}+\log K_m+o(1).
\tag{5}
\]

Thus the nth-root square condition `b_n->m^2` is still too compressed to decide the signed transition. The adjacent-packet ratio is selected at the next scale by `Xi_{n,m}`:

- if `Xi_{n,m}->-infinity`, then `F_{n,m}->0` and the `(m-1)`-column packet dominates;
- if `Xi_{n,m}->+infinity`, then `F_{n,m}->infinity` and the `m`-column packet dominates;
- if `Xi_{n,m}->xi in R`, then `F_{n,m}->K_m e^xi`.

For odd `n`, where the two AF-421 leading packets have opposite signs, **a necessary first-order tuning for their leading amplitudes to cancel is**

\[
\boxed{
\Xi_{n,m}\longrightarrow-\log K_m.
}
\tag{6}
\]

If `(6)` fails along an odd subsequence in any of the three regimes above, AF-421's two-packet reduction already decides the signed asymptotic: one packet dominates or the limiting bracket is nonzero. For even `n`, the packet signs agree and no adjacent-packet cancellation is possible.

For `m>=2`, put

\[
\Lambda_m
:=
L_{m-1}(m^2)
=
L_m(m^2)
=
\frac{m^{2m-2}}{((m-1)!)^2}>1.
\tag{7}
\]

Hence every square-transition sequence covered above **except the odd fine-tuned interface `(6)`** has

\[
\lim_{n\to\infty}|S_n^{(s_n)}(a)|^{1/n}=\Lambda_m
\tag{8}
\]

along the corresponding parity/subsequence whenever the stated `Xi` regime has a limit. In particular, the exceptional-`1` sector diverges exponentially rather than recovering the fixed-partition exponential.

There is a simple canonical corollary. On the exact square path

\[
a=m^2,\qquad s_n=2n,
\tag{9}
\]

one has `b_n=m^2`, `d_n=0`, and therefore

\[
\Xi_{n,m}=\log n,
\qquad
F_{n,m}\sim K_m n.
\tag{10}
\]

So the `m`-column packet beats the `(m-1)`-column packet by a linear factor. AF-421 then gives

\[
S_n^{(2n)}(m^2)
=
e^{-m^2e^2}(-1)^{mn}C_{n,m}(1+o(1)).
\tag{11}
\]

For `m>=2`, this diverges exponentially with nth-root rate `Lambda_m`. For `m=1`, `(3)` becomes

\[
K_1=\frac{24e^2}{\pi^2},
\]

and `(10)` recovers exactly AF-421's linear first-boundary asymptotic.

The fine-tuned interface `(6)` is **not** claimed to solve the square-transition problem. There `F_{n,m}->1`, and AF-421 only proves that each full-column rectangle packet carries a residual Schur-Cauchy factor tending to the same `e^{-ae^2}`. Once the leading rectangle amplitudes cancel, the difference between those residual packets and further subexponential terms can become decisive. The next unresolved object is therefore the ratio of the complete adjacent packets, not another refinement of the nth-root coordinate alone.

## 1. Exact reduction of the adjacent ratio

Starting from `(1)` and using `s_n=2n+d_n`, write

\[
a^n=b_n^n n^{-d_n}.
\]

Then `(1)` becomes the exact factorization

\[
F_{n,m}
=
n\left(\frac{b_n}{m^2}\right)^n
m^{1-d_n}
\left(1+\frac mn\right)^{2n+d_n-1}
\frac{\zeta(2(n+m))}{\zeta(2m)}
\left(2+\frac{2m-1}{n}\right)^2
\frac1{(2m-1)^2}.
\tag{12}
\]

Because `d_n=o(n)`,

\[
\left(1+\frac mn\right)^{2n+d_n-1}\longrightarrow e^{2m},
\tag{13}
\]

while

\[
\zeta(2(n+m))\longrightarrow1
\tag{14}
\]

and

\[
\left(2+\frac{2m-1}{n}\right)^2\longrightarrow4.
\tag{15}
\]

Collecting `(12)`--`(15)` gives

\[
F_{n,m}
=
\frac{4m e^{2m}}{(2m-1)^2\zeta(2m)}
\,n
\left(\frac{b_n}{m^2}\right)^n
m^{-d_n}
(1+o(1)),
\tag{16}
\]

which is exactly `(4)` after taking the logarithm of the three scale-sensitive factors.

The important point is that none of

\[
\log n,
\qquad
n\log(b_n/m^2),
\qquad
-d_n\log m
\]

is visible in the nth-root limit used to locate the square saddle. Their sum is precisely the information needed to decide the next packet ratio.

## 2. Signed consequence of the detuning coordinate

AF-421 gives at `b=m^2`

\[
S_n^{(s_n)}(a)
=
E(a)(-1)^{(m-1)n}C_{n,m-1}
\left[1+(-1)^nF_{n,m}\right]
+o(C_{n,m-1}+C_{n,m}),
\tag{17}
\]

where `E(a)=e^{-ae^2}` and `C_{n,m}=F_{n,m}C_{n,m-1}`.

If `n` is even, the bracket is `1+F_{n,m}` and cannot cancel. If `n` is odd, it is `1-F_{n,m}`. Equation `(4)` therefore converts the unresolved square transition into one explicit scalar detuning condition.

When `Xi_{n,m}->xi` with `K_m e^xi !=1`, division of `(17)` by `C_{n,m-1}` yields a nonzero limiting packet coefficient. When `Xi_{n,m}->-infinity`, `C_{n,m-1}` dominates; when it tends to `+infinity`, `C_{n,m}` dominates. Since both tied rectangles have nth-root rate `Lambda_m`, `(8)` follows for `m>=2`.

Only the odd interface `(6)` defeats this argument: there the coefficient `1-F_{n,m}` tends to zero, and the `o(C_{n,m-1}+C_{n,m})` remainder in AF-421 can no longer be discarded relative to the cancelled leading term.

## 3. Exact-square path closes every natural square boundary

Set `(9)`. Equation `(16)` immediately gives `(10)`. Since the ratio tends to infinity, `(17)` reduces to `(11)` independently of parity.

For `m>=2`, the common tied rate satisfies

\[
\Lambda_m
=
\left(\frac{m^{m-1}}{(m-1)!}\right)^2>1.
\tag{18}
\]

Thus every exact square path `a=m^2, s_n=2n` with `m>=2` is exponentially divergent. The case `m=1` is the degenerate endpoint `Lambda_1=1`; AF-421's sharper polynomial calculation supplies the linear divergence there.

This removes a potentially misleading interpretation of the square set `1,4,9,...`: a square nth-root tie does **not** by itself signal delicate cancellation. On the most natural exact-square sequence, the next-scale prefactor already separates the two saddles by a factor asymptotic to `K_m n`.

## 4. Arithmetic-fidelity interpretation

AF-420 retained `b_n` because the coarser limit `s_n/n->2` loses the critical `n/log n` displacement. AF-421 then showed that `b_n` selects a discrete full-column saddle but becomes non-discriminating at `b=m^2`. The present result identifies the next retained coordinate needed exactly on that collision fiber:

\[
(s_n/n)
\;\rightsquigarrow\;
b_n
\;\rightsquigarrow\;
\Xi_{n,m}
\;\rightsquigarrow\;
\text{complete-packet ratio on the tuned interface}.
\]

This is a concrete example of stratified fidelity under asymptotic compression. A statistic may be sufficient on an open stratum yet fail precisely on its transition locus; the correct lift is then not necessarily more global data, but the next subleading combination that the coarse limit quotiented out.

No rational-prime discriminator is obtained here and no RH consequence follows. The result sharpens only the varying-derivative exceptional-`1` sector inherited from AF-417--AF-421.

## Prior-art and novelty audit

The Schur-function, determinant-twist, Pieri, and Cauchy identities used to reach AF-421 are classical; AF-421 already places them against Macdonald's *Symmetric Functions and Hall Polynomials* and the Schur-measure/process literature of Okounkov and Okounkov--Reshetikhin. Bernoulli/Euler Hankel determinants and shifted sequences also have established literature, including the work of Dilcher and Jiu cited in AF-421.

The general warning that ordinary asymptotic expansions become nonuniform when dominant saddles collide is classical. Chester, Friedman, and Ursell, **“An extension of the method of steepest descents,”** *Proceedings of the Cambridge Philosophical Society* 53 (1957), 599--611, DOI `10.1017/S0305004100032655`, is a foundational uniform-asymptotic treatment of two nearly coincident saddle points. That literature supplies context for why a second scale can be necessary near a transition; it does not supply equations `(2)`--`(6)`, which are derived directly from AF-421's exact discrete adjacent-packet ratio.

A targeted search across coalescing-saddle asymptotics, Schur measures/processes, rectangular partition asymptotics, and Bernoulli/Euler shifted Hankel determinants did not locate this exact Euler-log derivative-Hankel ratio or the detuning coordinate `(2)`. **No novelty claim is made**: the durable content is the exact specialization and the resulting closure/narrowing of the current Mathia square-transition gate.

## Boundaries and falsification checks

- The theorem assumes the AF-421 finite critical window `s_n/n->2` and `b_n->m^2` for fixed `m`. It does not cover the genuinely supercritical regime `s_n/n->sigma>2`.
- `Xi_{n,m}` is a next-scale coordinate only on a fixed square fiber. It is not proposed as a universal compression invariant.
- Equation `(6)` is necessary for cancellation of the two leading rectangle amplitudes on odd `n`; it is not sufficient for cancellation of the **complete** adjacent packets.
- Once `(6)` holds, differences between the residual packets `G_{n,m}` and `G_{n,m-1}`, further partition profiles, or still finer scaling may decide the answer. No estimate in this finding suppresses those terms after leading cancellation.
- The exponential divergence statement `(8)` for `m>=2` uses AF-421's already-proved two-packet reduction. It must not be extrapolated to a sequence for which the bracket itself tends to zero at the unresolved tuned rate.
- The exact-square corollary `(11)` is stronger than an nth-root statement because `F_{n,m}~K_m n` prevents cancellation; it does not assert a full prefactor asymptotic for `C_{n,m}` beyond what AF-421 established.
- No statement about total positivity, rational-prime fidelity, zeta-zero location, or RH follows.

## Consequence for the research line

The finite-window square-transition frontier is now codimension one at the next scale. For every fixed `m>=2`, even subsequences and all odd subsequences with `Xi_{n,m}` not tuned to `-log K_m` are closed by exponential divergence. The canonical exact-square path is closed for every `m`, extending AF-421's explicit `m=1` boundary calculation.

The remaining finite-window question is narrower: on odd `n`, impose `(6)` and derive the asymptotic ratio of the **complete** adjacent packets, including the first difference between their residual Schur-Cauchy factors. That calculation, rather than another nth-root saddle classification, decides whether a genuinely fine-tuned square transition can cancel or merely exposes a still finer retained coordinate.