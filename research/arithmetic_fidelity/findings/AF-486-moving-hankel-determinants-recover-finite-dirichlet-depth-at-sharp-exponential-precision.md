# AF-486 — Moving Hankel determinants recover finite Dirichlet depth at sharp exponential precision

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SAMPLING`, `HANKEL-DETERMINANT`, `JOINT-RECOVERY`, `SHARP-NOISE-SCALE`, `CLASSICAL-PRONY`, `NO-BROAD-NOVELTY-CLAIM`

## Claim

AF-485 shows that any right-unbounded exact sample sequence is source-faithful for a discrete Dirichlet source, but its constructive proof peels atoms sequentially. AF-437 had already isolated the corresponding stability problem: recursive subtraction can amplify earlier reconstruction errors exponentially. A finite moving window of rightward samples admits a different, joint mechanism.

Let

\[
F(s)=\sum_{n\ge1} a_n q_n^{-s},
\qquad
1<q_1<q_2<\cdots\to\infty,
\qquad a_n>0,
\tag{1}
\]

converge absolutely for `Re(s)>sigma_0`. Fix a depth `J>=1` and a step `h>0`. For real `t>sigma_0`, define the `J x J` moving Hankel matrix

\[
H_J(t)
:=
\bigl[F(t+(r+s)h)\bigr]_{r,s=0}^{J-1},
\qquad
D_J(t):=\det H_J(t),
\qquad D_0(t):=1.
\tag{2}
\]

Then only the `2J-1` consecutive samples

\[
F(t),F(t+h),\ldots,F(t+(2J-2)h)
\]

are needed to form `D_J(t)`, and

\[
\boxed{
q_J
=
\lim_{t\to\infty}
\left(\frac{D_J(t)}{D_{J-1}(t)}\right)^{-1/t}.
}
\tag{3}
\]

More precisely, with

\[
x_n=q_n^{-h},
\qquad
Q_J:=\prod_{j=1}^J q_j,
\qquad
A_J:=
\left(\prod_{j=1}^J a_j\right)
\prod_{1\le i<j\le J}(x_i-x_j)^2,
\tag{4}
\]

one has

\[
\boxed{
D_J(t)
=A_J Q_J^{-t}
\left(1+O\!\left((q_J/q_{J+1})^{t-c}\right)\right)
}
\tag{5}
\]

for every fixed `c>sigma_0`, with the evident exact finite-source interpretation when there is no `q_{J+1}`. Consequently

\[
\frac{D_J(t)}{D_{J-1}(t)}
=
\frac{A_J}{A_{J-1}}q_J^{-t}(1+o(1)).
\tag{6}
\]

Thus the `J`th generator is exposed directly by a **joint determinant of a finite moving sample window** rather than by subtracting estimates of the first `J-1` atoms.

The mechanism also has a sharp exponential robustness scale. Write

\[
\widetilde F(t+kh)=F(t+kh)+\eta_k(t),
\qquad 0\le k\le2J-2,
\tag{7}
\]

with real adversarial errors, and form the corresponding Hankel determinants `\widetilde D_j(t)`. Let

\[
V_J=(x_j^r)_{0\le r\le J-1,\,1\le j\le J}
\]

and `a_{*,J}:=\min_{1\le j\le J}a_j`. If for all sufficiently large `t`

\[
\max_k|\eta_k(t)|
\le
\varepsilon q_J^{-t}
\quad\text{with}\quad
0<\varepsilon<\frac{a_{*,J}\sigma_{\min}(V_J)^2}{J},
\tag{8}
\]

then

\[
\boxed{
q_J
=
\lim_{t\to\infty}
\left(\frac{\widetilde D_J(t)}{\widetilde D_{J-1}(t)}\right)^{-1/t}.
}
\tag{9}
\]

So fixed finite depth `J` is stably recoverable from a moving window at **absolute precision of order `q_J^{-t}`**, up to a source-dependent separation/conditioning constant. That exponential scale is unavoidable in the adversarial model: an error vector of exactly the `J`th atom's contribution,

\[
\eta_k(t)=-a_Jq_J^{-(t+kh)},
\tag{10}
\]

removes that atom from the entire observed window. Hence no uniform theorem can recover the `J`th generator under unrestricted adversarial errors whose size is allowed to be an order-one multiple of `q_J^{-t}`.

For the ordinary prime-zeta source `F=P`, where `a_n=1` and `q_n=p_n`, equation `(9)` gives a concrete finite-depth statement: the first `J` rational primes are recoverable from a sequence of `2J-1`-sample rightward windows when the absolute error is controlled on the scale `p_J^{-t}`. This does not distinguish rational primes from other positive discrete generators; it quantifies the source-information scale at which the `J`th ordered generator survives the compression.

## Exact Hankel/Vandermonde expansion

From `(1)` and `x_n=q_n^{-h}`,

\[
F(t+(r+s)h)
=
\sum_{n\ge1} a_n q_n^{-t}x_n^{r+s}.
\tag{11}
\]

Thus

\[
H_J(t)
=
\sum_{n\ge1}a_n q_n^{-t}v_nv_n^T,
\qquad
v_n=(1,x_n,\ldots,x_n^{J-1})^T.
\tag{12}
\]

For a finite truncation, Cauchy-Binet gives

\[
D_{J,N}(t)
=
\sum_{1\le n_1<\cdots<n_J\le N}
\left(\prod_{r=1}^J a_{n_r}q_{n_r}^{-t}\right)
\prod_{1\le r<s\le J}(x_{n_r}-x_{n_s})^2.
\tag{13}
\]

Absolute convergence of `F(c)` for any fixed `c>sigma_0` makes the infinite subset sum finite, while the finite Hankel matrices converge entrywise to `(2)`. Passing `N\to\infty` therefore yields

\[
\boxed{
D_J(t)
=
\sum_{|S|=J}
\left(\prod_{n\in S}a_nq_n^{-t}\right)
\Delta(x_S)^2,
}
\tag{14}
\]

where `\Delta(x_S)` is the Vandermonde product on the selected nodes.

Every term in `(14)` is nonnegative. Since the generators are strictly increasing, the unique subset with smallest generator product is

\[
S_0=\{1,\ldots,J\},
\qquad
Q_{S_0}=Q_J.
\]

Its coefficient is exactly `A_J>0` from `(4)`.

## Dominance of the first `J` generators

For every non-leading `J`-subset `S`,

\[
Q_S:=\prod_{n\in S}q_n
\ge
q_1\cdots q_{J-1}q_{J+1},
\]

so

\[
\frac{Q_J}{Q_S}
\le
\rho_J:=\frac{q_J}{q_{J+1}}<1.
\tag{15}
\]

Fix `c>sigma_0`. For `t\ge c`,

\[
\left(\frac{Q_J}{Q_S}\right)^t
\le
\rho_J^{t-c}
\left(\frac{Q_J}{Q_S}\right)^c.
\tag{16}
\]

The weighted subset sum at exponent `c` is finite because, using `\Delta(x_S)^2\le1`,

\[
\sum_{|S|=J}
\prod_{n\in S}a_nq_n^{-c}\Delta(x_S)^2
\le
\frac1{J!}
\left(\sum_{n\ge1}a_nq_n^{-c}\right)^J
<\infty.
\tag{17}
\]

Dividing `(14)` by the leading term and applying `(16)`-`(17)` proves `(5)`. Applying the same result at depth `J-1` gives `(6)`, and taking `-1/t` powers proves `(3)`. The fixed coefficient `A_J/A_{J-1}` disappears under the root.

The same asymptotic contains the amplitudes in the zero-noise case. Once the nodes `q_1,\ldots,q_J` are known,

\[
\lim_{t\to\infty}
q_J^t\frac{D_J(t)}{D_{J-1}(t)}
=
\frac{A_J}{A_{J-1}}
=
a_J\prod_{i<J}(q_i^{-h}-q_J^{-h})^2.
\tag{18}
\]

Hence the positive amplitude `a_J` is also recoverable. Unlike the generator root limit, however, amplitude recovery needs relative determinant accuracy tending to zero; a merely bounded multiplicative determinant error is not enough to preserve the constant in `(18)`.

## Stability without recursive peeling

Take the first `J` source atoms in `(12)` and form the square Vandermonde matrix `V_J`. Positivity gives the Loewner lower bound

\[
H_J(t)
\succeq
V_J\operatorname{diag}(a_1q_1^{-t},\ldots,a_Jq_J^{-t})V_J^T.
\tag{19}
\]

Because `q_i\le q_J` for `i\le J`,

\[
\lambda_{\min}(H_J(t))
\ge
a_{*,J}q_J^{-t}\sigma_{\min}(V_J)^2.
\tag{20}
\]

Let `E_J(t)=\widetilde H_J(t)-H_J(t)`. Every entry of `E_J` is one of the sample errors in `(7)`, so `(8)` implies

\[
\|E_J(t)\|_2
\le
J\varepsilon q_J^{-t}.
\tag{21}
\]

Therefore

\[
K_J(t):=H_J(t)^{-1/2}E_J(t)H_J(t)^{-1/2}
\]

satisfies

\[
\|K_J(t)\|_2
\le
\kappa_J
:=
\frac{J\varepsilon}{a_{*,J}\sigma_{\min}(V_J)^2}
<1.
\tag{22}
\]

Since the perturbation is real symmetric,

\[
\widetilde D_J(t)
=D_J(t)\det(I+K_J(t))
\]

and hence

\[
(1-\kappa_J)^J
\le
\frac{\widetilde D_J(t)}{D_J(t)}
\le
(1+\kappa_J)^J.
\tag{23}
\]

The multiplicative error is bounded above and below by positive constants independent of `t`. Its `1/t` power therefore tends to `1`.

For `D_{J-1}`, the same sample error bound is even smaller relative to the weakest retained atom, because

\[
\frac{q_J^{-t}}{q_{J-1}^{-t}}
=
\left(\frac{q_{J-1}}{q_J}\right)^t
\to0.
\tag{24}
\]

Thus `\widetilde D_{J-1}(t)/D_{J-1}(t)\to1` in the corresponding relative operator bound. Combining this with `(6)` and `(23)` proves `(9)`.

This is the key difference from recursive peeling. AF-437 shows that estimating a later shell by repeatedly subtracting previously estimated larger contributions can force earlier errors to be exponentially finer at every stage. Here all first-`J` contributions enter one positive Gram matrix, and the `J`th scale is protected by its smallest singular direction. Earlier atoms need not first be reconstructed and subtracted from the samples.

## Sharpness of the exponential noise scale

The sufficient constant in `(8)` depends on the conditioning of the first-`J` Vandermonde matrix and is not claimed optimal. The **exponential order** `q_J^{-t}`, however, cannot be improved in the adversarial model.

For every offset `k=0,\ldots,2J-2`, choose the error `(10)`. Then

\[
\widetilde F(t+kh)
=
F(t+kh)-a_Jq_J^{-(t+kh)},
\tag{25}
\]

which is exactly the same moving observation window produced by deleting the `J`th atom from the source.

If the original source has at least `J+1` atoms, the perturbed data are therefore compatible with a positive source whose first `J` generators are

\[
q_1,\ldots,q_{J-1},q_{J+1},
\]

so no decoder seeing only these noisy samples can be guaranteed to return the original `q_J`. If the source has exactly `J` atoms, deletion drops the Hankel rank below `J` and makes the `J`th determinant vanish.

Moreover

\[
\max_k|\eta_k(t)|=a_Jq_J^{-t},
\tag{26}
\]

because `q_J^{-h}<1`. Thus an adversary can erase the target atom with error precisely on the same exponential scale as the sufficient theorem. The remaining gap is only in the source-dependent constant, controlled on the sufficient side by weight and Vandermonde separation.

## Relationship to AF-437, AF-444/445, and AF-485

This result does not replace the earlier moment findings.

AF-444 and AF-445 study **static finite moment identifiability thresholds** for finite atomic source classes. Their Newton and shifted-Hankel certificates determine how many moments are required to separate source cardinalities when nuisance supports and weights vary. The present theorem instead studies an **infinite positive Dirichlet source**, a fixed finite window whose location moves to the right, and asymptotic separation of the ordered leading atoms by exponential scale.

AF-485 establishes exact injectivity from any countable right-unbounded sample sequence by least-exponent domination. Its explicit reconstruction is sequential. AF-437 shows why the analogous recursive shell-peeling strategy can be badly conditioned. Equation `(9)` supplies the missing joint alternative for any fixed depth: the moving Hankel determinant combines `2J-1` nearby samples before taking the asymptotic limit, so finite-depth recovery is controlled directly at the weakest retained signal scale `q_J^{-t}`.

The improvement is therefore not that exponential precision disappears. It cannot, by `(25)`-`(26)`. The improvement is that **the precision budget is tied to the deepest atom one actually wants to retain, rather than being compounded by a recursive chain of earlier subtraction errors.**

## Prior art and novelty audit

The algebraic machinery is classical. Positive exponential sums and finite atomic moment sequences have standard Hankel/Vandermonde factorizations, and Prony-type reconstruction uses exactly this structured moment geometry. Dmitry Batenkov and Yosef Yomdin, **“On the Accuracy of Solving Confluent Prony Systems,”** *SIAM Journal on Applied Mathematics* 73(1), 134–154 (2013), DOI `10.1137/110836584`, studies local stability of Prony-type systems under measurement error and explicitly places Hankel and confluent-Vandermonde structure at the center of the conditioning problem. Classical Vandermonde factorization of Hankel matrices and finite exponential-sum reconstruction are therefore not claimed as new.

The determinant expansion `(14)` is also a direct Cauchy-Binet identity; its use for positive atomic moment matrices is standard moment/Prony mathematics. No novelty is claimed for Cauchy-Binet, positivity of Gram matrices, Vandermonde determinants, or extraction of finite exponential nodes from sufficiently rich exact moment data.

The Arithmetic Fidelity contribution is the **specific moving-rightward Dirichlet-source boundary** obtained by combining those classical tools with AF-485's ordered exponential asymptotics and AF-437's stability obstruction: a fixed `2J-1`-sample moving window recovers the `J`th ordered generator through a determinant ratio, arbitrary tail atoms are suppressed at the explicit gap rate `(q_J/q_{J+1})^t`, and adversarial sample precision of exponential order `q_J^{-t}` is both sufficient up to conditioning constants and necessary up to constants. The claim is this source/compression/fidelity synthesis, not a new Prony algorithm.

## Boundaries and falsification checks

- Positivity of the amplitudes is essential to the clean Gram lower bound, nonnegative Cauchy-Binet expansion, and unique dominant-subset argument. Signed or complex amplitudes can cancel determinant contributions and require a separate analysis.
- The generators must be strictly increasing and discrete. Repeated generators should first be merged into one positive amplitude; accumulating exponent support falls outside the proof.
- `J` and `h>0` are fixed while `t\to\infty`. No condition number uniform in `J` is claimed. The Vandermonde factor `\sigma_{\min}(V_J)` can be very small when retained nodes nearly collide.
- The sufficient error constant in `(8)` is conservative and source-dependent. Only the exponential order `q_J^{-t}` is shown sharp by `(25)`-`(26)`.
- Equation `(9)` recovers the generator under bounded adversarial real errors at the declared scale. Stable recovery of the amplitude `a_J` needs stronger relative accuracy, for example `o(q_J^{-t})` at depth `J`, because the amplitude lives in the non-root constant `(18)`.
- The theorem uses a moving family of sample windows with base point escaping to `+infinity`; it does not contradict AF-484, which proves non-faithfulness of every fixed finite family of samples.
- The result is source-fidelity, not rational-prime fidelity. Every positive discrete Beurling/Dirichlet source obeying the hypotheses has the same recovery mechanism. Nothing here distinguishes the ordinary primes from matched generalized primes or implies RH.
- Downstream transforms such as zeta continuation, spectra, determinants of unrelated operators, positivity certificates, or asymptotic scalarizations do not automatically inherit this fidelity. The theorem applies to the declared raw Dirichlet sample window.

A direct falsification would require either a non-leading `J`-subset whose generator product is no larger than `q_1\cdots q_J`, contradicting strict ordering, or an admissible perturbation satisfying `(8)` that makes the positive definite matrix `I+K_J` singular or changes the determinant ratio by an exponential factor. Bounds `(15)` and `(22)` rule out those two mechanisms respectively.

## Research consequence

The quantitative frontier after AF-485 is no longer simply “how accurate must every peeling step be?” For fixed depth, there is a canonical joint observable whose conditioning can be audited directly. The retained information scale is

\[
\boxed{
\text{depth }J
\quad\longleftrightarrow\quad
\text{absolute sample scale }q_J^{-t}
\times
\text{Vandermonde/source-separation constant}.
}
\tag{27}
\]

This gives a concrete fidelity law: rightward compression does not destroy the first `J` ordered source atoms, but the `J`th atom survives only at its own exponentially small amplitude scale. The next useful question is whether arithmetic source constraints can improve the **conditioning constant** or reduce the required moving-window width without reintroducing recursive error amplification; the exponential depth scale itself cannot be removed under unrestricted adversarial noise.